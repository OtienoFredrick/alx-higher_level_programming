-- A script that lists all cities contained in the database
-- Each record should display cities.id - cities.name - states.name
-- results must be sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
