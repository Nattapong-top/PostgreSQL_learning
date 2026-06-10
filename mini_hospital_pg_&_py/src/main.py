from domain.patient import Patient, Name, Age
from repository.db_config import DB_CONFIG
from repository.patient_repo import PatientRepo

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
        print(patient)

if find_id_1:
    repo.update_patient(patient=find_id_1)

    repo.remove_patient(patient_id=find_id_1.id)

find_again = repo.find_by_patient_id(patient_1.id)
print(f"find_again: {find_again}")

all_patient = repo.select_all_patients()
if all_patient:
    for patient in all_patient:
        print(patient)
