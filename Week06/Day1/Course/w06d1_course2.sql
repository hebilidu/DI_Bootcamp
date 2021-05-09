-- SELECT * FROM actors;

-- ALTER TABLE actors
-- ADD COLUMN gender CHAR(1);

-- ALTER TABLE actors
-- ADD CONSTRAINT gender_constraint CHECK (gender = 'M' or gender = 'F');

-- UPDATE actors 
-- SET 
--  	gender = 'G'
-- WHERE
--  	actor_id IN (3);

-- ALTER TABLE actors
-- ALTER COLUMN gender SET NOT NULL;

-- SELECT * FROM actors
-- LIMIT 4

-- SELECT * FROM actors
-- ORDER BY last_name DESC
-- LIMIT 4;

-- SELECT * FROM actors
-- WHERE last_name LIKE '%e%'

-- SELECT * from actors
-- WHERE number_oscars >= 5;