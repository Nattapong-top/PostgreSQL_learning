from datetime import datetime

from domain.patient import Patient, Name, Age, PatientID
from domain.queue import Queue, QueueStatus
from repository.db_config import DB_CONFIG
from repository.patient_repo import PatientRepo
from repository.queue_repo import QueueRepo

patient_1 = Patient(
    first_name=Name(value="Patient1"),
    last_name=Name(value="Patient1"),
    age=Age(value=20),
)

repo = PatientRepo(db_config=DB_CONFIG)
repo.add_patient(patient_1)

find_id_1 = repo.find_by_patient_id(patient_1.id)
print(f"find_id_1: {find_id_1}")
all_patient = repo.select_all_patients()

if all_patient:
    for patient in all_patient:
        print(
            patient.id.id,
            patient.first_name.value,
            patient.last_name.value,
            patient.age.value,
        )

if find_id_1:
    repo.update_patient(patient=find_id_1)

    repo.remove_patient(patient_id=find_id_1.id)

find_again = repo.find_by_patient_id(patient_1.id)
print(f"find_again: {find_again}")

all_patient = repo.select_all_patients()
if all_patient:
    for patient in all_patient:
        print(
            patient.id.id,
            patient.first_name.value,
            patient.last_name.value,
            patient.age.value,
        )


patient_2 = Patient(
    first_name=Name(value="Patient2"),
    last_name=Name(value="Patient2"),
    age=Age(value=22),
)
print(patient_2.id, patient_2.first_name, patient_2.last_name)

queue = Queue(
    patient_id=PatientID(id=patient_2.id.id),
    queue_number=1,
    status=QueueStatus.waiting,
    created_at=datetime.now(),
)

print(f"queue: {queue}")
q_repo = QueueRepo(db_config=DB_CONFIG)
q_repo.add_queue(queue)

print(queue.id.id)

find_q1 = q_repo.find_by_queue_id(queue.id)
print(f"find_q1: {find_q1}")
q_repo.update_status(queue=queue, status=QueueStatus.in_progress)
update_q1 = q_repo.find_by_queue_id(queue.id)
print(f"update_q1: {update_q1}")

find_all = q_repo.find_all_queue()
# print(f"find_all: {find_all}")
