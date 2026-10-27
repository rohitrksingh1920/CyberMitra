
from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator,
    model_validator,
)

from app.models import ComplaintStatus, CrimeType


# Complaints

class ComplaintCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    contact_number: str = Field(min_length=6, max_length=20)
    incident_date: Optional[str] = Field(default=None, max_length=40)
    crime_type: CrimeType = CrimeType.OTHER
    description: str = Field(min_length=10, max_length=5000)
    evidence_notes: Optional[str] = Field(default=None, max_length=3000)

    @field_validator("contact_number")
    @classmethod
    def basic_phone_check(cls, v: str) -> str:
        digits = "".join(ch for ch in v if ch.isdigit())
        if len(digits) < 6:
            raise ValueError("contact_number does not look valid")
        return v


# Internal/admin representation. Never use this for public tracking responses.
class ComplaintPublic(BaseModel):
    reference_code: str
    name: str
    contact_number: str
    incident_date: Optional[str]
    crime_type: CrimeType
    description: str
    evidence_notes: Optional[str]
    status: ComplaintStatus
    created_at: datetime

    model_config = {"from_attributes": True}


# Minimal response returned after a public submission and from public tracking.
class ComplaintTrackingPublic(BaseModel):
    reference_code: str
    status: ComplaintStatus
    created_at: datetime

    model_config = {"from_attributes": True}


class ComplaintAdminUpdate(BaseModel):
    status: Optional[ComplaintStatus] = None
    admin_notes: Optional[str] = Field(default=None, max_length=3000)


# Suspect checker

class SuspectCheckRequest(BaseModel):
    value: str = Field(min_length=3, max_length=200)
    entity_type: str = Field(pattern=r"^(phone|upi|url)$")

    @field_validator("value")
    @classmethod
    def validate_value(cls, value: str) -> str:
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Identifier must contain at least 3 characters")
        if any(ord(ch) < 32 for ch in value):
            raise ValueError("Identifier contains invalid control characters")
        return value


class SuspectCheckResponse(BaseModel):
    found: bool
    report_count: int = 0
    last_category: Optional[str] = None
    message: str


class SuspectReportCreate(BaseModel):
    value: str = Field(min_length=3, max_length=200)
    entity_type: str = Field(pattern=r"^(phone|upi|url)$")
    reporter_token: str = Field(
        pattern=r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
    )
    category: str | None = Field(default=None, max_length=100)
    notes: str | None = Field(default=None, max_length=1000)

    @field_validator("value")
    @classmethod
    def validate_value(cls, value: str) -> str:
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Identifier must contain at least 3 characters")
        if any(ord(ch) < 32 for ch in value):
            raise ValueError("Identifier contains invalid control characters")
        return value

    @field_validator("category", "notes")
    @classmethod
    def clean_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return None

        value = value.strip()
        if not value:
            return None

        if any(ord(ch) < 32 and ch not in "\n\r\t" for ch in value):
            raise ValueError("Text contains invalid control characters")

        return value


# Contact

class ContactCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    subject: Optional[str] = Field(default=None, max_length=200)
    message: str = Field(min_length=5, max_length=3000)


# Quiz

class QuizResultCreate(BaseModel):
    score: int = Field(ge=0)
    total: int = Field(gt=0)
    name: Optional[str] = Field(default=None, max_length=120)

    @model_validator(mode="after")
    def validate_score(self):
        if self.score > self.total:
            raise ValueError("Score cannot exceed total questions")
        return self


# Pledge

class PledgeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    city: Optional[str] = Field(default=None, max_length=120)