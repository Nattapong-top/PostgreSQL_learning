--🔥 ด่านที่ 1: รายงานขั้นสุด (Phase 1: Subquery + JOIN + Aggregate)
--สถานการณ์: ผู้อำนวยการโรงพยาบาลต้องการดูรายงาน "แพทย์ที่ทำงานหนักเกินมาตรฐาน" เพื่อพิจารณาเพิ่มโบนัส
--Requirement: ป๋าต้องเขียน Query เพื่อหา "ชื่อหมอ (full_name)" และ "จำนวนคิวทั้งหมดที่หมอคนนั้นรับ" โดยมีเงื่อนไขว่า หมอคนนั้นจะต้องมีจำนวนคิวรวม "มากกว่าค่าเฉลี่ย" ของจำนวนคิวที่พนักงานทุกคนรับ
--
--(คำใบ้: ข้อนี้ป๋าต้องใช้ความสามารถของ JOIN เพื่อเชื่อมตาราง หา COUNT ของคิว อัดด้วย GROUP BY และต้องใช้ HAVING คู่กับ Subquery เพื่อเทียบกับค่าเฉลี่ยรวม)

SELECT full_name, COUNT(queues.id) FROM staff
LEFT JOIN queues ON staff.id = queues.staff_id
GROUP BY full_name
HAVING  COUNT(queues.id) > (SELECT AVG(q_count) FROM (
    SELECT COUNT(id) AS q_count
    FROM queues
    GROUP BY staff_id
 ) AS temp_table
);