SELECT queue_number, status, first_name, last_name
FROM queues
INNER JOIN patients
ON queues.patient_id = patients.id;

SELECT queue_number, first_name, full_name
FROM queues
INNER JOIN patients
ON queues.patient_id = patients.id
INNER JOIN staff
ON queues.staff_id = staff.id;


SELECT queue_number, first_name, full_name
FROM queues
LEFT JOIN patients
ON queues.patient_id = patients.id
LEFT JOIN staff
ON queues.staff_id = staff.id;

SELECT queue_number, first_name
FROM queues
FULL OUTER JOIN patients
ON queues.patient_id = patients.id;

SELECT * FROM patients ORDER BY id ASC;


--
--สรุปแบบ "ใช้จริงในชีวิต"
--INNER JOIN — ใช้เมื่อต้องการข้อมูลที่ครบทั้งสองฝั่งเท่านั้น เช่น "queue ที่มีทั้งคนไข้ และ staff แล้ว"
--LEFT JOIN — ใช้บ่อยที่สุดในชีวิตจริง เช่น "queue ทั้งหมด ไม่ว่าจะมี staff หรือยัง" → ป๋าทำไปแล้วใน ข้อ 5.3
--RIGHT JOIN — แทบไม่ใช้ เพราะเขียน LEFT JOIN กลับด้านได้เหมือนกัน ส่วนใหญ่เจอในโค้ดเก่าเท่านั้น
--FULL OUTER JOIN — ใช้ตอน audit ข้อมูล เช่น "หา patient ที่ไม่เคยมี queue เลย และ queue ที่ไม่มี patient เลย"

