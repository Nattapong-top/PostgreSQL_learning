SELECT role, COUNT(*) FROM staff
GROUP BY role
HAVING COUNT(*) > 1;

SELECT status, COUNT(*) FROM queues
GROUP BY status
HAVING COUNT(*) >= 2;

--💡 WHERE vs HAVING — จำง่ายๆ
--SELECT role, COUNT(*)
--FROM staff            ← WHERE กรองตรงนี้ (ก่อนนับ)
--WHERE role != 'doctor'
--GROUP BY role
--HAVING COUNT(*) > 1   ← HAVING กรองตรงนี้ (หลังนับแล้ว)
--
--ถามตัวเองว่า — "กรองก่อนหรือหลังนับ?"
--ก่อนนับ → WHERE / หลังนับ → HAVING