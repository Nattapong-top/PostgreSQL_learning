CREATE TABLE queues (
    id SERIAL PRIMARY KEY,

    -- 2. Foreign Keys (ฟอเรน-คีย์ = กุญแจเชื่อมต่างตาราง)
    patient_id INTEGER NOT NULL,
    staff_id INTEGER,

    -- 3. ข้อมูล Queue
    queue_number INTEGER NOT NULL,
    status VARCHAR(50) NOT NULL,

    -- 4. Timestamp (ไทม์สแตมป์ = เวลาที่บันทึก)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- 5. CONSTRAINT (คอนสเทรนต์ = กฎข้อบังคับ)
    CONSTRAINT fk_patient
        FOREIGN KEY(patient_id)
        REFERENCES patients(id),

    CONSTRAINT fk_staff
        FOREIGN KEY(staff_id)
        REFERENCES staff(id)
);
