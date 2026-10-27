from fastapi import APIRouter, Depends, Request, HTTPException
from sqlmodel import Session, select

from sqlalchemy.dialects.postgresql import insert as pg_insert

from app.database import get_session
from app.models import SuspectEntity, SuspectReportLog, utcnow
from app.schemas import SuspectCheckRequest, SuspectCheckResponse, SuspectReportCreate
from app.utils.normalize import normalize_entity
from app.limiter import limiter

router = APIRouter(prefix="/suspects", tags=["Suspect Checker"])


@router.post("/check", response_model=SuspectCheckResponse)
@limiter.limit("20/minute")
def check_suspect(request: Request, payload: SuspectCheckRequest, session: Session = Depends(get_session)):
    """Check whether a phone number, UPI ID, or URL has been reported by
    other CyberMitra users before. This is community-sourced data, not an
    official government blocklist — always verify independently."""
    normalized = normalize_entity(payload.value, payload.entity_type)
    entity = session.exec(
        select(SuspectEntity).where(
            SuspectEntity.value == normalized, SuspectEntity.entity_type == payload.entity_type
        )
    ).first()

    if not entity:
        return SuspectCheckResponse(
            found=False,
            report_count=0,
            message="No reports found for this yet. That doesn't guarantee it's safe — stay cautious.",
        )

    return SuspectCheckResponse(
        found=True,
        report_count=entity.report_count,
        last_category=entity.last_category,
        message=f"⚠ This has been reported {entity.report_count} time(s) by other users. Proceed with caution.",
    )



# @router.post("/report", status_code=201)
# @limiter.limit("10/minute")
# def report_suspect(
#     request: Request,
#     payload: SuspectReportCreate,
#     session: Session = Depends(get_session),
# ):
#     """Record a community report while safely updating the aggregate."""
#     normalized = normalize_entity(payload.value, payload.entity_type)

#     try:
#         # Insert a new aggregate, or atomically increment an existing one.
#         statement = (
#             pg_insert(SuspectEntity)
#             .values(
#                 value=normalized,
#                 entity_type=payload.entity_type,
#                 report_count=1,
#                 last_category=payload.category,
#                 created_at=utcnow(),
#                 updated_at=utcnow(),
#             )
#             .on_conflict_do_update(
#                 index_elements=["value", "entity_type"],
#                 set_={
#                     "report_count": SuspectEntity.report_count + 1,
#                     "last_category": (
#                         payload.category
#                         if payload.category is not None
#                         else SuspectEntity.last_category
#                     ),
#                     "updated_at": utcnow(),
#                 },
#             )
#         )

#         session.exec(statement)

#         # Retain an individual audit record for every submission.
#         log = SuspectReportLog(
#             entity_value=normalized,
#             entity_type=payload.entity_type,
#             category=payload.category,
#             notes=payload.notes,
#         )
#         session.add(log)
#         session.commit()

#         return {
#             "message": "Thanks — this has been logged to help warn other users.",
#             "value": normalized,
#         }

#     except Exception:
#         session.rollback()
#         raise



@router.post("/report", status_code=201)
@limiter.limit("10/minute")
def report_suspect(
    request: Request,
    payload: SuspectReportCreate,
    session: Session = Depends(get_session),
):
    """Record a report once per anonymous browser token and identifier."""
    normalized = normalize_entity(payload.value, payload.entity_type)

    try:
        # First, attempt to record this token's report.
        # The unique database index makes this safe against concurrent
        # repeated submissions using the same token and identifier.
        log_statement = (
            pg_insert(SuspectReportLog)
            .values(
                entity_value=normalized,
                entity_type=payload.entity_type,
                reporter_token=payload.reporter_token,
                category=payload.category,
                notes=payload.notes,
                created_at=utcnow(),
            )
            .on_conflict_do_nothing(
                index_elements=[
                    "entity_value",
                    "entity_type",
                    "reporter_token",
                ]
            )
            .returning(SuspectReportLog.id)
        )

        inserted = session.exec(log_statement).first()

        if inserted is None:
            session.rollback()
            return {
                "message": (
                    "You have already reported this identifier "
                    "from this browser."
                ),
                "value": normalized,
                "already_reported": True,
            }

        # Increment the aggregate only if the individual report was new.
        aggregate_statement = (
            pg_insert(SuspectEntity)
            .values(
                value=normalized,
                entity_type=payload.entity_type,
                report_count=1,
                last_category=payload.category,
                created_at=utcnow(),
                updated_at=utcnow(),
            )
            .on_conflict_do_update(
                index_elements=["value", "entity_type"],
                set_={
                    "report_count": SuspectEntity.report_count + 1,
                    "last_category": (
                        payload.category
                        if payload.category is not None
                        else SuspectEntity.last_category
                    ),
                    "updated_at": utcnow(),
                },
            )
        )

        session.exec(aggregate_statement)
        session.commit()

        return {
            "message": "Thank you. Your report has been recorded.",
            "value": normalized,
            "already_reported": False,
        }

    except Exception:
        session.rollback()
        raise