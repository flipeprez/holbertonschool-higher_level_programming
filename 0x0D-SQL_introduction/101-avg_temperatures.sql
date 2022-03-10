-- Write a script that displays the average temperature
SELECT City, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
