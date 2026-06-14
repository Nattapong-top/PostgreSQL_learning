from uuid import uuid4, UUID

from datetime import datetime
from enum import Enum
from pydantic import Field

from domain.patient import PatientID, BaseID, DomainModel


class QueueID(BaseID):
    id: UUID = Field(default_factory=uuid4)


class QueueStatus(Enum):
    waiting = "waiting"
    in_progress = "in_progress"
    complete = "complete"
    canceled = "canceled"


class Queue(DomainModel):
    id: QueueID = Field(default_factory=QueueID)
    patient_id: PatientID
    queue_number: int = Field(..., gt=0)
    status: QueueStatus = QueueStatus.waiting
    created_at: datetime = Field(default_factory=datetime.now)
