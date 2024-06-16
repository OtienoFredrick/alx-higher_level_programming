-- Import in hbtn the database temprature.sql
-- Write a script that displays the average temprature
-- by city ordered by temprature in descending

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
