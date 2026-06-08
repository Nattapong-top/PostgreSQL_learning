from domain.patient import Patient, Name, Age
from repository.db_config import DB_CONFIG
from repository.patient_repo import PatientRepo

patient_1 = Patient(
    first_name=Name(value="Patient1"),
    last_name=Name(value="Patient1"),
    age=Age(value=20)
)


repo = PatientRepo(db_config=DB_CONFIG)
repo.add_patient(patient_1)


find_id_1 = repo.find_by_patient_id(patient_1.id)
print(find_id_1)