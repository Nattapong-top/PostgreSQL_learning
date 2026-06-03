CREATE TABLE queues (
    id SERIAL PRIMARY KEY,

    patient_id INTEGER NOT NULL,
    staff_id INTEGER,

    queue_number INTEGER NOT NULL,
    status VARCHAR(50) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_patient
        FOREIGN KEY(patient_id)
        REFERENCES patients(id),

    CONSTRAINT fk_staff
        FOREIGN KEY(staff_id)
        REFERENCES staff(id)
);
