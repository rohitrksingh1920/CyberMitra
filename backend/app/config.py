
"""
Central configuration for the CyberMitra backend.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator


class Settings(BaseSettings):
    # App
    APP_NAME: str = "CyberMitra API"
    ENV: str = "development"
    API_V1_PREFIX: str = "/api"

    # Database: supply DATABASE_URL through environment variables.
    DATABASE_URL: str = ""

    # Comma-separated allowed origins.
    CORS_ORIGINS: str = "http://localhost:5173,http://127.0.0.1:5173"

    # Admin key must be supplied outside source code.
    ADMIN_API_KEY: str = ""

    # Rate limiting
    RATE_LIMIT_DEFAULT: str = "60/minute"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @property
    def cors_origins_list(self) -> list[str]:
        return [
            origin.strip().rstrip("/")
            for origin in self.CORS_ORIGINS.split(",")
            if origin.strip()
        ]

    @model_validator(mode="after")
    def validate_production_settings(self):
        if self.ENV.lower() == "production":
            if not self.DATABASE_URL:
                raise ValueError(
                    "DATABASE_URL must be set in production"
                )

            if (
                not self.ADMIN_API_KEY
                or self.ADMIN_API_KEY == "change-this-admin-key"
                or len(self.ADMIN_API_KEY) < 32
            ):
                raise ValueError(
                    "Set a strong ADMIN_API_KEY of at least 32 characters"
                )

            if not self.CORS_ORIGINS.strip():
                raise ValueError(
                    "CORS_ORIGINS must be configured in production"
                )

            if "*" in self.cors_origins_list:
                raise ValueError(
                    "Wildcard CORS origins are not allowed in production"
                )

        return self


settings = Settings()
