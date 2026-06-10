from datetime import date
from enum import Enum
from pydantic import Field

from domain.patient import PatientID, BaseID, DomainModel


class QueueID(BaseID):
    pass


class QueueStatus(Enum):
    waiting = "waiting"
    in_progress = "in_progress"
    complete = "complete"
    canceled = "canceled"


class Queue(DomainModel):
    id: QueueID = Field(default_factory=QueueID)
    patient_id: PatientID
    queue_name: int
    status: QueueStatus
    created_at: date
