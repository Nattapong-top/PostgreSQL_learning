from abc import ABC, abstractmethod

from domain.patient import Patient, PatientID
from domain.queue import Queue


class PatientABC(ABC):
    @abstractmethod
    def add_patient(self, patient: Patient) -> None:
        pass

    @abstractmethod
    def find_by_patient_id(self, patient_id: int) -> Patient | None:
        pass

class QueueABC(ABC):
    @abstractmethod
    def save(self, patient: Patient) -> Queue:
        pass

    @abstractmethod
    def find_by_patient_id(self, patient_id: PatientID) -> Patient | None:
        pass

    @abstractmethod
    def find_all(self) -> list[Queue]:
        pass