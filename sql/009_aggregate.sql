SELECT COUNT(*) FROM patients;

SELECT AVG(age), MAX(age), MIN(age) FROM patients;

SELECT status, COUNT(*) FROM queues GROUP BY status;



SELECT role, COUNT(*) FROM staff GROUP BY role;













-- GROUP BY + Aggregate Functions
--(แอ็กกริเกต-ฟังก์ชัน = ฟังก์ชันรวมข้อมูลหลาย row เป็นค่าเดียว)
--Function    ความหมาย        ตัวอย่าง
--COUNT(*)    นับจำนวน row     มีคนไข้กี่คน
--AVG()       หาค่าเฉลี่ย        อายุเฉลี่ย
--MAX()       หาค่ามากสุด       อายุมากสุด
--MIN()       หาค่าน้อยสุด       อายุน้อยสุด
--SUM()       รวมทั้งหมด        รวม queue ทั้งหมด