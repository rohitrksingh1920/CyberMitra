# from fastapi import APIRouter, Depends, Request
# from sqlmodel import Session, select

# from app.database import get_session
# from app.models import ContactMessage, QuizResult, PledgeSignature
# from app.schemas import ContactCreate, QuizResultCreate, PledgeCreate
# from app.limiter import limiter

# router = APIRouter(tags=["Misc"])


# @router.post("/contact", status_code=201)
# @limiter.limit("5/minute")
# def submit_contact(request: Request, payload: ContactCreate, session: Session = Depends(get_session)):
#     msg = ContactMessage(**payload.model_dump())
#     session.add(msg)
#     session.commit()
#     return {"message": "Thanks for reaching out — we'll get back to you soon."}


# @router.post("/quiz/results", status_code=201)
# def submit_quiz_result(payload: QuizResultCreate, session: Session = Depends(get_session)):
#     result = QuizResult(**payload.model_dump())
#     session.add(result)
#     session.commit()
#     return {"message": "Score recorded", "score": payload.score, "total": payload.total}


# @router.get("/quiz/stats")
# def quiz_stats(session: Session = Depends(get_session)):
#     results = session.exec(select(QuizResult)).all()
#     if not results:
#         return {"attempts": 0, "average_score_pct": None}
#     total_pct = sum((r.score / r.total) * 100 for r in results if r.total)
#     return {
#         "attempts": len(results),
#         "average_score_pct": round(total_pct / len(results), 1),
#     }


# @router.post("/pledge", status_code=201)
# def submit_pledge(payload: PledgeCreate, session: Session = Depends(get_session)):
#     sig = PledgeSignature(**payload.model_dump())
#     session.add(sig)
#     session.commit()
#     return {"message": "Pledge recorded. Thank you for committing to safer digital habits."}


# @router.get("/pledge/count")
# def pledge_count(session: Session = Depends(get_session)):
#     count = len(session.exec(select(PledgeSignature)).all())
#     return {"count": count}








from fastapi import APIRouter, Depends, Request
from sqlalchemy import func
from sqlmodel import Session, select

from app.database import get_session
from app.models import ContactMessage, QuizResult, PledgeSignature
from app.schemas import ContactCreate, QuizResultCreate, PledgeCreate
from app.limiter import limiter

router = APIRouter(tags=["Misc"])


@router.post("/contact", status_code=201)
@limiter.limit("5/minute")
def submit_contact(
    request: Request,
    payload: ContactCreate,
    session: Session = Depends(get_session),
):
    msg = ContactMessage(**payload.model_dump())
    session.add(msg)
    session.commit()
    return {
        "message": "Thanks for reaching out — we'll get back to you soon."
    }


@router.post("/quiz/results", status_code=201)
@limiter.limit("10/minute")
def submit_quiz_result(
    request: Request,
    payload: QuizResultCreate,
    session: Session = Depends(get_session),
):
    result = QuizResult(**payload.model_dump())
    session.add(result)
    session.commit()
    return {
        "message": "Score recorded",
        "score": payload.score,
        "total": payload.total,
    }


@router.get("/quiz/stats")
@limiter.limit("30/minute")
def quiz_stats(
    request: Request,
    session: Session = Depends(get_session),
):
    attempts = session.exec(
        select(func.count(QuizResult.id))
    ).one()

    average_pct = session.exec(
        select(
            func.avg(
                QuizResult.score * 100.0 / QuizResult.total
            )
        )
    ).one()

    return {
        "attempts": attempts,
        "average_score_pct": (
            round(float(average_pct), 1)
            if average_pct is not None
            else None
        ),
    }


@router.post("/pledge", status_code=201)
@limiter.limit("5/minute")
def submit_pledge(
    request: Request,
    payload: PledgeCreate,
    session: Session = Depends(get_session),
):
    sig = PledgeSignature(**payload.model_dump())
    session.add(sig)
    session.commit()
    return {
        "message": (
            "Pledge recorded. Thank you for committing "
            "to safer digital habits."
        )
    }


@router.get("/pledge/count")
@limiter.limit("30/minute")
def pledge_count(
    request: Request,
    session: Session = Depends(get_session),
):
    count = session.exec(
        select(func.count(PledgeSignature.id))
    ).one()

    return {"count": count}
