EXPLAIN SELECT * FROM patients WHERE first_name = 'John';

CREATE INDEX idx_patients_first_name ON patients(first_name);

EXPLAIN SELECT * FROM patients WHERE first_name = 'John';