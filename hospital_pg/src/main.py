import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
DB_CONFIG = {
    "host": os.getenv('DB_HOST'),
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASSWORD'),
    "database": os.getenv('DB_NAME'),
    "port": os.getenv('DB_PORT')
}

# การเชื่อมต่อ pg แบบ ธรรมดา
# # conn = None
# # cur = None
#
# try:
#     conn = psycopg2.connect(
#         host="localhost",
#         user="postgres",
#         password="password",
#         database="hospital_pg",
#         port="5432"
#     )
#
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM patients')
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
# finally:
#     if conn:
#         conn.close()
#     if cur:
#         cur.close()

print('block with '+'-'*20)

def add_patient(first_name:str, last_name:str, age:int) -> None:
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO patients (first_name, last_name, age) "
                            "VALUES (%s, %s, %s)", (first_name, last_name, age))
                conn.commit()
                print('เพิ่มคนไข้สำเร็จ')
    except Exception as e:
        conn.rollback()
        print(f'เพิ่มคนข้อมูลไข้ไม่สำเร็จ เกิด error ย้อนกลับแล้ว: {e}')

add_patient('สมปอง', 'รักสุภาพ', 25)

# การเชื่อมต่อ pg แบบ block with ไม่ต้อง close()
def select_patient_all():
    with psycopg2.connect(**DB_CONFIG) as conn:

        with conn.cursor() as cur:
            cur.execute('SELECT * FROM patients')
            rows = cur.fetchall()
            for row in rows:
                print(row)
select_patient_all()

def update_patient(patient_id:int, first_name:str, last_name:str, age:int) -> None:
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE patients SET first_name=%s, last_name=%s, age=%s WHERE id=%s ",
                            (first_name, last_name, age, patient_id))
                conn.commit()
                print('แก้ไขข้อมูลคนไข้สำเร็จ')
    except Exception as e:
        conn.rollback()
        print(f'แก้ไขข้อมูลคนไข้ไม่สำเร็จ เกิด error ย้อนกลับแล้ว: {e}')

update_patient(patient_id=4, first_name='สมปอง', last_name='น้องสมชาย', age=37)
update_patient(patient_id='sdfg', first_name='สมปอง', last_name='น้องสมชาย', age=37)
select_patient_all()

def delete_patient(patient_id:int) -> None:
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM patients WHERE id=%s", (patient_id,))
                conn.commit()
                print('ลบข้อมูลคนไข้สำเร็จ')
    except Exception as e:
        conn.rollback()
        print(f'ลบข้อมูลคนไข้ไม่สำเร็จ เกิด error ย้อนกลับแล้ว: {e}')

delete_patient(patient_id=3)
delete_patient(patient_id='sdfg')
select_patient_all()

def get_patient_by_id(patient_id:int):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM patients WHERE id=%s', (patient_id,))
            row = cur.fetchone()
            if row is None:
                return None
            return row

select_patient_all()
id_4 = get_patient_by_id(patient_id=4)
print(id_4)
id_3 = get_patient_by_id(patient_id=3)
print(id_3)


def add_patient_and_error_handling(first_name:str, last_name:str, age:int) -> None:
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO patients (first_name, last_name, age)'
                            'VALUES (%s, %s, %s)', (first_name, last_name, age))
                conn.commit()
                print('เพิ่มคนไข้สำเร็จ')
    except Exception as e:
        conn.rollback()
        print(f'เพิ่มข้อมูลคนไข้ไม่สำเร็จ เกิด error ย้อนกลับแล้ว: {e}')

add_patient_and_error_handling(first_name=12312323, last_name=12312323, age='sfgsfg')