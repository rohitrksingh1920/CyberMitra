

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.config import settings
from app.database import init_db
from app.limiter import limiter
from app.routers import complaints, suspects, misc


# Never allow the API to start in production with a known/default admin key.
if settings.ENV.lower() == "production":
    unsafe_admin_keys = {
        "devkey",
        "change-this-admin-key",
        "change_me_to_a_long_random_string",
    }
    if not settings.ADMIN_API_KEY or settings.ADMIN_API_KEY.strip().lower() in unsafe_admin_keys:
        raise RuntimeError("A unique, strong ADMIN_API_KEY is required in production.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


is_production = settings.ENV.lower() == "production"


app = FastAPI(
    title=settings.APP_NAME,
    description=(
        "Backend API for CyberMitra — Cyber Security Awareness, "
        "Assistance and Reporting Platform."
    ),
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    # This application uses explicit headers; cookie credentials are not enabled by default.
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "X-Admin-Key"],
)

app.include_router(complaints.router, prefix=settings.API_V1_PREFIX)
app.include_router(suspects.router, prefix=settings.API_V1_PREFIX)
app.include_router(misc.router, prefix=settings.API_V1_PREFIX)


@app.get("/api/health")
def health_check():
    # Do not disclose deployment environment details in the public health response.
    return {"status": "ok", "service": settings.APP_NAME}

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Welcome to CyberMitra API",
        "docs": "/docs"
    }


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    # Keep internal exception details out of public responses.
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error. Please try again shortly."},
    )
