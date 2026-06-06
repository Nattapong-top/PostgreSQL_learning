--🎁 เกร็ดความรู้ที่ใช้บ่อยจริงๆ
--
--1. RETURNING — ดูค่าหลัง INSERT/UPDATE ทันที
--sql-- ปกติ INSERT แล้วไม่รู้ว่าได้ id อะไร
INSERT INTO doctor (full_name, username, age, license_no)
VALUES ('สมชาย', 'somchai', 40, '1234567890')
RETURNING id, username;

-- ผลลัพธ์
-- id | username
------+----------
--  3 | somchai
--
--ใช้บ่อยมากตอนเขียน Repository ค่ะ เพราะ Python ต้องรู้ id ที่ได้หลัง INSERT
--
--
--2. UPSERT — INSERT ถ้าไม่มี UPDATE ถ้ามีอยู่แล้ว
sqlINSERT INTO doctor (full_name, username, age, license_no)
VALUES ('สมชาย', 'somchai', 40, '1234567890')
ON CONFLICT (username)           -- ถ้า username ซ้ำ
DO UPDATE SET age = EXCLUDED.age; -- อัปเดตแทน error

--EXCLUDED = ค่าที่พยายาม INSERT เข้ามาค่ะ


--3. COALESCE — จัดการ NULL ให้สวยงาม
--sql-- NULL แสดงผลน่าเกลียด
SELECT queue_number, full_name FROM queues LEFT JOIN staff ...
-- full_name = NULL

-- ใช้ COALESCE แทนค่า NULL
SELECT queue_number, COALESCE(full_name, 'ยังไม่มีหมอ') AS full_name
FROM queues LEFT JOIN staff ...
-- full_name = 'ยังไม่มีหมอ'

--COALESCE(ค่า, ค่าสำรอง) = ถ้าค่าแรก NULL → ใช้ค่าสำรองแทน


--4. ALIAS — ตั้งชื่อย่อ table ให้ SQL สั้นลง
--sql-- ❌ พิมพ์เยอะมาก
SELECT patients.first_name, queues.status
FROM queues
INNER JOIN patients ON queues.patient_id = patients.id;

-- ✅ ใช้ alias
SELECT p.first_name, q.status
FROM queues q
INNER JOIN patients p ON q.patient_id = p.id;

--5. LIMIT + OFFSET — ทำ Pagination
--sql-- หน้า 1: 10 rows แรก
SELECT * FROM patients LIMIT 10 OFFSET 0;

-- หน้า 2: 10 rows ถัดไป
SELECT * FROM patients LIMIT 10 OFFSET 10;

-- หน้า 3
SELECT * FROM patients LIMIT 10 OFFSET 20;

--ใช้ทุกครั้งที่ทำ API ที่มีการแบ่งหน้าค่ะ


--6. NOW() — เวลาปัจจุบัน
--sql-- บันทึกเวลาตอน update
UPDATE doctor SET updated_at = NOW() WHERE id = 1;

-- หา queue ที่สร้างวันนี้
SELECT * FROM queues
WHERE created_at >= NOW() - INTERVAL '1 day';

--7. DISTINCT — กรองค่าซ้ำออก
--sql-- ดู role ทั้งหมดที่มีอยู่ (ไม่ซ้ำ)
SELECT DISTINCT role FROM staff;

-- ผลลัพธ์
-- role
--------
-- doctor
-- nurse

--💡 ทริคใน psql ที่ใช้บ่อย
--bash\timing        # เปิดจับเวลาทุก query
--\e             # เปิด editor แก้ query ยาวๆ
--\x             # เปลี่ยน format แสดงผลแนวตั้ง (อ่านง่ายกว่า)
--\i sql/001.sql # รัน SQL file จากใน psql ได้เลย
--
--\x มีประโยชน์มากตอน column เยอะๆ ค่ะ:
---- ปกติ (อ่านยาก)
--id | first_name | last_name | age
-----+------------+-----------+----
-- 1 | John       | Doe       | 35
--
---- หลัง \x (อ่านง่าย)
--id         | 1
--first_name | John
--last_name  | Doe
--age        | 35