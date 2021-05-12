-- week 06 day 4 - Course
-- COPY actors(first_name,last_name,birthdate,number_oscars,gender,cntry_id) FROM '/Users/lidu/Development/GitHub/di/DI_Bootcamp/Week06/Day4/actor_data.csv' DELIMITER ';' CSV HEADER;

-- SELECT * FROM actors;

-- DELETE FROM actors WHERE actor_id IN (12);

-- From psql:
-- hollywood=# \copy actors(first_name,last_name,birthdate,number_oscars,gender) FROM '/Users/lidu/Development/GitHub/di/DI_Bootcamp/Week06/Day4/actor_data2.csv' WITH CSV HEADER; 

-- *** Without function:
-- SELECT CONCAT(first_name,' ',last_name) fullname from actors;

-- With function:
-- CREATE OR REPLACE FUNCTION fullname_actor (fn varchar(50), lan varchar(100)) RETURNS VARCHAR(100) AS $fullname$
-- BEGIN
--     RETURN (SELECT CONCAT(first_name,' ',last_name) FROM actors WHERE actors.first_name = fn AND actors.last_name = lan);
-- END
-- $fullname$ LANGUAGE plpgsql;

-- SELECT * FROM fullname_actor('Matt', 'Damon');

-- *** Display the age of a given actor, without function:
-- SELECT EXTRACT (year FROM NOW()) - EXTRACT (year FROM birthdate) FROM actors;

-- Same with function:
-- CREATE or REPLACE FUNCTION current_age_actor(fn varchar(50), lan varchar(100)) RETURNS int AS $current_age$
-- declare
--     current_age integer;
--     birth_date date;
--     now_date date := CURRENT_DATE;
-- BEGIN
--    birth_date := (SELECT birthdate FROM actors WHERE actors.first_name = fn AND actors.last_name = lan);
--    current_age := DATE_PART('year', now_date) - DATE_PART('year', birth_date);
--    RETURN current_age;
-- END;
-- $current_age$ LANGUAGE plpgsql;

-- SELECT * FROM current_age_actor('Matt', 'Damon');

-- *** Function that outputs number of letters in the firstname of an actor:

-- CREATE or REPLACE FUNCTION count_actor_fname_letters(fn varchar(50), lan varchar(100)) RETURNS int AS $cnt_fname_letters$
-- BEGIN
--     RETURN LENGTH(fn);
-- END;
-- $cnt_fname_letters$ LANGUAGE plpgsql;

-- SELECT * FROM count_actor_fname_letters('Matt', 'Damon');
-- SELECT * FROM count_actor_fname_letters('Tom', 'Holland');

-- *** Print fullname of employees which add up to 10 characters
SELECT CONCAT(first_name,' ',last_name) FROM actors
WHERE LENGTH(CONCAT(first_name,' ',last_name)) = 10;

-- *** Print nb of films in each category:
