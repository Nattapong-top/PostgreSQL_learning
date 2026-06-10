from uuid import UUID, uuid4
from pydantic import Field, BaseModel, ConfigDict


class DomainModel(BaseModel):
    model_config = ConfigDict(frozen=True)


class BaseID(DomainModel):
    id: UUID


class PatientID(BaseID):
    id: UUID = Field(default_factory=uuid4)


class Name(DomainModel):
    value: str = Field(..., min_length=1, max_length=100)


class Age(DomainModel):
    value: int = Field(..., ge=0, le=150)


class Patient(DomainModel):
    id: PatientID = Field(default_factory=PatientID)
    first_name: Name
    last_name: Name
    age: Age
