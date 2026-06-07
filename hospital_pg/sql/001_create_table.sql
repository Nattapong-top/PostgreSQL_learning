CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INTEGER
);

INSERT INTO patients (
    first_name,
    last_name,
    age
)
VALUES
('สมชาย', 'รักษาหาย', 60),
('สมหญิง', 'รักษาอยู่', 59),
('สมคิด', 'รักษาแล้ว', 30);


SELECT * FROM patients;