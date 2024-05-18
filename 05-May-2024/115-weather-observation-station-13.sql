-- TITLE: WEATHER OBSERVATION STATION 13
-- TASK: Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345. Truncate your answer to 4 decimal places.
-- SOURCE: https://www.hackerrank.com/challenges/weather-observation-station-13
-- 18 May 2024

SELECT ROUND(SUM(lat_n), 4)
FROM station
WHERE lat_n > 38.7880 AND lat_n < 137.2345;