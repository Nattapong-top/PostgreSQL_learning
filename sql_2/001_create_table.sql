CREATE TABLE patients_2 (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INTEGER,
    created_at TIMESTAMP
);

CREATE TABLE staff_2 (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    position VARCHAR(100),
    salary NUMERIC,
    is_active BOOLEAN,
    created_at TIMESTAMP
);