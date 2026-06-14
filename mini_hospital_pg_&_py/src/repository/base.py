from abc import ABC, abstractmethod

from domain.patient import Patient, PatientID
from domain.queue import Queue, QueueID, QueueStatus


class PatientABC(ABC):
    @abstractmethod
    def add_patient(self, patient: Patient) -> None:
        pass

    @abstractmethod
    def find_by_patient_id(self, patient_id: PatientID) -> Patient | None:
        pass

    @abstractmethod
    def select_all_patients(self) -> list[Patient]:
        pass

    @abstractmethod
    def update_patient(self, patient: Patient) -> None:
        pass

    @abstractmethod
    def remove_patient(self, patient_id: PatientID) -> None:
        pass


class QueueABC(ABC):
    @abstractmethod
    def add_queue(self, patient: Patient) -> None:
        pass

    @abstractmethod
    def update_status(self, queue_id: QueueID,  status: QueueStatus) -> None:
        pass

    @abstractmethod
    def find_by_patient_id(self, patient_id: PatientID) -> Patient | None:
        pass

    @abstractmethod
    def find_by_queue_id(self, queue_id: QueueID) -> Patient | None:
        pass

    @abstractmethod
    def find_all_queue(self) -> list[Queue] | None:
        pass
