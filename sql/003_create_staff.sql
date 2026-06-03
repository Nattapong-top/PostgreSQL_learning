CREATE TABLE staff (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(200) NOT NULL,
    role VARCHAR(50) NOT NULL
);

INSERT INTO staff (
    username,
    full_name,
    role
)
VALUES
('dr.somchai', 'นพ.สมชาย ใจดี', 'doctor'),
('nurse.malee', 'พย.มาลี รักงาน', 'nurse'),
('rec.noi', 'น้อย ตอนรับดี', 'receptionist');


SELECT * FROM staff WHERE role = 'doctor';