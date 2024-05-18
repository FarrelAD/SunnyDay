-- TITLE: WEATHER OBSERVATION STATION 2
-- TASK: Query the following two values from the STATION table:
--       1. The sum of all values in LAT_N rounded to a scale of  decimal places.
--       2. The sum of all values in LONG_W rounded to a scale of  decimal places.
-- SOURCE: https://www.hackerrank.com/challenges/weather-observation-station-2
-- 18 May 2024


SELECT ROUND(SUM(lat_n), 2), ROUND(SUM(long_w), 2)
FROM station;