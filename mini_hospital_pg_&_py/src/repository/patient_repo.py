import psycopg2

from domain.patient import Patient, PatientID, Name, Age
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

    UPDATE_PATIENT = """
    UPDATE patient SET first_name=%s, last_name=%s, age=%s WHERE id=%s
    """

    DELETE_PATIENT = """
    DELETE FROM patient WHERE id=%s
    """

    SELECT_ALL_PATIENTS = """
    SELECT * FROM patient ORDER BY id DESC LIMIT 5
    """

    def __init__(self, db_config: dict) -> None:
        self.db_config = db_config
        self.auto_create_patient_table()

    def auto_create_patient_table(self):
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute(self.AUTO_CREATE_PATIENT_TABLE)
                conn.commit()
                print("created patient table successfully")

    def add_patient(self, patient: Patient) -> None:
        try:
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        self.INSERT_INTO_PATIENT,
                        (
                            str(patient.id.id),
                            patient.first_name.value,
                            patient.last_name.value,
                            patient.age.value,
                        ),
                    )
                    conn.commit()
                    print(f"added patient {patient.first_name.value} successfully")
        except Exception as err:
            conn.rollback()
            print(f"failed to add patient {patient.first_name.value} to patient table")
            print(f"error: {err}")

    def find_by_patient_id(self, patient_id: PatientID) -> Patient | None:
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute(self.SELECT_PATIENT_ID, (str(patient_id.id),))
                patient = cur.fetchone()

                if not patient:
                    return None

                p_id, first_name, last_name, age = patient
                patient_entity = Patient(
                    id=PatientID(id=p_id),
                    first_name=Name(value=first_name),
                    last_name=Name(value=last_name),
                    age=Age(value=age),
                )

                return patient_entity

    def update_patient(self, patient: Patient) -> None:

        data = (
            patient.first_name.value,
            patient.last_name.value,
            patient.age.value,
            str(patient.id.id),
        )

        try:
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(self.UPDATE_PATIENT, data)
                    print(f"updated patient {patient.first_name.value} successfully")
                    conn.commit()
        except Exception as err:
            conn.rollback()
            print(
                f"failed to update patient {patient.first_name.value} to patient table"
            )
            print(f"error: {err}")

    def remove_patient(self, patient_id: PatientID) -> None:
        try:
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(self.DELETE_PATIENT, (str(patient_id.id),))
                    conn.commit()
                    print(f"deleted patient {patient_id.id} successfully")
        except Exception as err:
            conn.rollback()
            print(f"failed to delete patient {patient_id.id} to patient table")
            print(f"error: {err}")

    def select_all_patients(self) -> list[Patient] | None:
        try:
            patients = []
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:

                    cur.execute(self.SELECT_ALL_PATIENTS)

                    for row in cur.fetchall():
                        p_id, first_name, last_name, age = row
                        patients.append(
                            Patient(
                                id=PatientID(id=p_id),
                                first_name=Name(value=first_name),
                                last_name=Name(value=last_name),
                                age=Age(value=age),
                            )
                        )

            return patients

        except Exception as err:
            print("failed to select all patients from patient table")
            print(f"error: {err}")
            return None
