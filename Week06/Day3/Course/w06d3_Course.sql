-- CREATE TABLE countries (
--     country_id SERIAL,
--     country_name VARCHAR(30),
--     PRIMARY KEY (country_id)
-- );

-- SELECT * FROM actors;

-- INSERT INTO countries (country_name)
-- VALUES ('France'), ('Belgium'), ('Israel'), ('USA'), ('Vietnam');

-- SELECT * 
-- FROM actors
-- INNER JOIN countries
-- ON countries.country_id = actors.actor_id;

-- SELECT * 
-- FROM actors
-- LEFT JOIN countries
-- ON countries.country_id = actors.actor_id;

-- SELECT * 
-- FROM actors
-- RIGHT JOIN countries
-- ON countries.country_id = actors.actor_id;

-- SELECT * 
-- FROM actors
-- FULL JOIN countries
-- ON countries.country_id = actors.actor_id;

-- CREATE TABLE scenarios (
--   pk_movie_id INTEGER NOT NULL,
--   scenario_story TEXT NOT NULL,
--   PRIMARY KEY (pk_movie_id),
--   CONSTRAINT fk_movie_id FOREIGN KEY (pk_movie_id) REFERENCES movies (movie_id)
-- );

-- ALTER TABLE actors
-- ADD cntry_id SMALLINT;

-- ALTER TABLE actors
-- ADD CONSTRAINT cntry_id  
-- FOREIGN KEY (cntry_id) 
-- REFERENCES countries (country_id);


-- SELECT * FROM countries;
-- INSERT INTO countries (country_id, country_name)
-- VALUES (0, 'unknown');
-- SELECT * FROM countries;

-- SELECT * FROM actors;
-- UPDATE actors
-- SET cntry_id = 0;
-- SELECT * FROM actors;

-- SELECT *
-- FROM (
--     SELECT * FROM actors
-- ) AS t;

SELECT * FROM (VALUES (1,'a'), (2,'b')) t(a,b);