-- a script that displays the average temperature (Fahrenheit)

SELECT city, AVG(value) as avg_temp FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
