INSERT INTO patients (
    first_name,
    last_name,
    age
)
VALUES
('ผู้ป่วย', 'อยากหาย', 20),
('หายป่วย', 'กลับบ้านได้', 60),
('หาหมอ', 'รักษา', 70);

SELECT * FROM patients;

SELECT first_name, last_name FROM patients;

SELECT * FROM patients WHERE age > 28;

SELECT * FROM patients ORDER BY age ASC;

SELECT * FROM patients LIMIT 2;