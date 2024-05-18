-- TITLE: WEATHER OBSERVATION STATION 6
-- TASK: Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
-- SOURCE: https://www.hackerrank.com/challenges/weather-observation-station-6
-- 16 May 2024

-- 1st method
SELECT DISTINCT city 
FROM station
WHERE city LIKE 'a%'
    OR city LIKE 'i%'
    OR city LIKE 'u%'
    OR city LIKE 'e%'
    OR city LIKE 'o%';


-- 2nd method
SELECT DISTINCT city 
FROM station
WHERE city REGEXP '^[aiueo]';