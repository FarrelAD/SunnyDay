-- TITLE: WEATHER OBSERVATION STATION 11
-- TASK: Query the list of CITY names from STATION that either do not start with vowels AND do not end with vowels. Your result cannot contain duplicates.
-- SOURCE: https://www.hackerrank.com/challenges/weather-observation-station-11
-- 17 May 2024

-- 1st method
SELECT DISTINCT city
FROM station
WHERE city NOT REGEXP '^[aeiou].*[aiueo]$';