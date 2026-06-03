SELECT * FROM patients
WHERE age > (SELECT AVG(age) FROM patients);

SELECT * FROM patients
WHERE id IN (SELECT patient_id FROM queues);

SELECT * FROM patients
WHERE id  NOT IN (SELECT patient_id FROM queues);


--สรุป 3 แบบ
--ประเภท          คืนค่า                  ใช้เมื่อ
--scalar         ค่าเดียว เช่น 36.25        WHERE age > (AVG)
--in             list เช่น (1, 2, 3)     WHERE id IN (...)
--not in         list เช่น (1, 2, 3)     WHERE id NOT IN (...)