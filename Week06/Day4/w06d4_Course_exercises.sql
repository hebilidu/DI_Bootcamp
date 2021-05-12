-- *** week 06 day 4 - Exercises on dvdrental

-- *** Count the number of movies in each category:
-- SELECT c.name, COUNT(fc.category_id) FROM film_category fc
-- INNER JOIN category c ON c.category_id = fc.category_id
-- GROUP BY c.name;

-- *** Full name of manager staff:
-- SELECT CONCAT(first_name,' ',last_name) FROM staff 
-- INNER JOIN store ON store.manager_staff_id = staff.staff_id;

-- *** Number of actors in Airport Pollock:
-- SELECT COUNT(*) AS number_actors_in_Airport_Pollock FROM film_actor fa
-- INNER JOIN film f ON f.film_id = fa.film_id
-- INNER JOIN actor a ON a.actor_id = fa.actor_id
-- WHERE f.title = 'Airport Pollock';

-- *** Print amounts paid each year:
-- SELECT EXTRACT (MONTH FROM payment_date) month_2007, SUM(amount) payment_sum
-- FROM payment
-- GROUP BY EXTRACT (MONTH FROM payment_date);

-- *** SELECT WITHIN SELECT
SELECT first_name FROM
(SELECT * FROM actor) AS subquery;

