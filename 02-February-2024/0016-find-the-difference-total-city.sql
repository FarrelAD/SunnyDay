-- TITLE: QUERY JAPANESE CITIES
-- TASK : Find the difference between the total number of CITY entries in the table 
--        and the number of distinct CITY entries in the table.
-- Source: https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true
-- 3 February 2024

-- Below is the SQL code
SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION