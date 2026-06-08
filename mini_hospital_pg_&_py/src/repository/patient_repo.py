import psycopg2
from typing import Any

from domain.patient import Patient, PatientID
from repository.base import PatientABC


class PatientRepo(PatientABC):
    AUTO_CREATE_PATIENT_TABLE = """
    CREATE TABLE IF NOT EXISTS patient (
        id UUID PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
        )
    """

    INSERT_INTO_PATIENT = """
    INSERT INTO patient (id, first_name, last_name, age) 
    VALUES (%s, %s, %s, %s)
    """

    SELECT_PATIENT_ID = """ SELECT * FROM patient WHERE id=%s """

    def __init__(self, db_config: dict) -> None:
        self.db_config = db_config
        self.auto_create_patient_table()

    def auto_create_patient_table(self):
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute(self.AUTO_CREATE_PATIENT_TABLE)
                print('created patient table successfully')

    def add_patient(self, patient: Patient) -> None:
        try:
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(self.INSERT_INTO_PATIENT,
                                (str(patient.id.id), patient.first_name.value, patient.last_name.value,
                                 patient.age.value))
                    print(f'added patient {patient.first_name.value} successfully')
        except Exception as err:
            print(f'failed to add patient {patient.first_name.value} to patient table')
            print(f'error: {err}')

    def find_by_patient_id(self, patient_id: PatientID) -> tuple[Any, ...] | None:
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute(self.SELECT_PATIENT_ID, (str(patient_id.id),)
                            )
                patient = cur.fetchone()
                return patient if patient else None
