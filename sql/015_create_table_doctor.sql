CREATE TABLE doctor (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    age INTEGER CHECK (age >= 18 AND age <= 80),
    license_no VARCHAR(10) UNIQUE NOT NULL CHECK (license_no <> '')
);

INSERT INTO doctor (
    full_name,
    username,
    age,
    license_no
)
VALUES
('raksadee smith', 'raksadee', 40, '1234567890'),
('smith raksadee', 'smith', 30, '0987654321');
-- check error
INSERT INTO doctor (
    full_name,
    username,
    age,
    license_no
)
VALUES
('smith raksadee', 'smith', 30, '1987654321');

INSERT INTO doctor (
    full_name,
    username,
    age,
    license_no
)
VALUES
('smith raksadee', 'smith_2', 17, '1987654322');


INSERT INTO doctor (
    full_name,
    username,
    age,
    license_no
)
VALUES
('smith raksadee', 'smith_3', 30, '');

INSERT INTO doctor (
    full_name,
    username,
    age,
    license_no
)
VALUES
('smith raksadee', 'smith_4', 30, '0987654321');

