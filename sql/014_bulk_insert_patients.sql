CREATE TABLE patients_test (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INTEGER
);

INSERT INTO patients_test (
    first_name,
    last_name,
    age
)
SELECT
    'patient_' || g,
    'Test',
    (random() * 80)::integer
FROM generate_series(1, 100000) AS g;

SELECT COUNT(*) FROM patients_test;

EXPLAIN ANALYZE
SELECT * FROM patients_test WHERE first_name = 'patient_50000';

CREATE INDEX idx_patients_test_first_name
ON patients_test(first_name);

EXPLAIN ANALYZE
SELECT * FROM patients_test WHERE first_name = 'patient_50000';
