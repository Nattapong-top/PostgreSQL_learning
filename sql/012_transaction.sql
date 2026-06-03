DELETE FROM patients WHERE first_name = 'รักษาหาย';
BEGIN;
    INSERT INTO patients (
        first_name,
        last_name,
        age
    )
    VALUES
    ('รักษาหาย', 'เป็นปกติ', 80);
    SELECT * FROM patients WHERE first_name = 'รักษาหาย';
    UPDATE patients SET age = 99 WHERE first_name = 'รักษาหาย';
COMMIT;

SELECT * FROM patients ORDER BY id ASC;


BEGIN;
    INSERT INTO patients (
    first_name,
    last_name,
    age
    )
    VALUES
    ('สุขภาพดี', 'ไม่ป่วยเลย', 150);
    SELECT * FROM patients WHERE first_name = 'สุขภาพดี';
ROLLBACK;

SELECT * FROM patients ORDER BY id ASC;