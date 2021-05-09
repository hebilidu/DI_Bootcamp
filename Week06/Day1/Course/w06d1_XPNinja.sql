-- Display all students :
-- SELECT * FROM students ORDER BY id;
-- First four students sorted by last_name :
-- SELECT * FROM students ORDER BY last_name ASC LIMIT 4;
-- Youngest student :
-- SELECT * FROM students ORDER BY birth_date DESC LIMIT 1;
-- Fetch 3 students skipping the first 2 :
SELECT * FROM students ORDER BY id OFFSET 2 LIMIT 3;
