
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.openapi.docs import get_redoc_html

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

    if (
        not settings.ADMIN_API_KEY
        or settings.ADMIN_API_KEY.strip().lower() in unsafe_admin_keys
    ):
        raise RuntimeError(
            "A unique, strong ADMIN_API_KEY is required in production."
        )


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    description=(
        "Backend API for CyberMitra — Cyber Security Awareness, "
        "Assistance and Reporting Platform."
    ),
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/openapi.json",
)


# Rate limiting
app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler,
)


# CORS: Register only ONCE.
allowed_origins = list(
    set(settings.cors_origins_list)
    | {
        "https://cybermitra-frontend.vercel.app",
        "http://localhost:5173",
        "http://localhost:3000",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ReDoc documentation
@app.get(
    "/redoc",
    include_in_schema=False,
    response_class=HTMLResponse,
)
async def redoc_html():
    response = get_redoc_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - ReDoc",
        redoc_js_url=(
            "https://cdn.redoc.ly/redoc/v3.x/"
            "bundles/redoc.standalone.js"
        ),
        with_google_fonts=False,
    )

    return HTMLResponse(content=response.body)


# API routers
app.include_router(
    complaints.router,
    prefix=settings.API_V1_PREFIX,
)

app.include_router(
    suspects.router,
    prefix=settings.API_V1_PREFIX,
)

app.include_router(
    misc.router,
    prefix=settings.API_V1_PREFIX,
)


# Health check
@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
    }


# Root endpoint
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Welcome to CyberMitra API",
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/api/health",
    }


# Global exception handler
@app.exception_handler(Exception)
async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
):
    return JSONResponse(
        status_code=500,
        content={
            "detail": (
                "Internal server error. Please try again shortly."
            )
        },
    )
