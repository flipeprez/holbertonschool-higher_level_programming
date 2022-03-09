-- write a script that lists all the cities of california.
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id = states.id;
