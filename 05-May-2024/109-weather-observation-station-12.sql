-- TITLE: WEATHER OBSERVATION STATION 12
-- TASK: Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
-- SOURCE: https://www.hackerrank.com/challenges/weather-observation-station-12
-- 17 May 2024

-- 1st method
SELECT DISTINCT city
FROM station
WHERE city NOT REGEXP '^[aiueo]' 
    AND city NOT REGEXP '[aiueo]$';