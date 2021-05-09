-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
-- 	('Liaam','Neeson','06/07/1952', 0),
-- 	('Uma','Thurman','04/29/1970', 0),
-- 	('Morgan','Freeman','06/01/1937', 1);

-- SELECT * FROM actors WHERE actor_id = 2;

-- UPDATE actors 
-- SET 
--     first_name = 'George',
-- 	last_name = 'Clooney',
-- 	age = '06/05/1961'
-- WHERE
--     actor_id = 2;

SELECT * FROM actors ORDER BY actor_id;