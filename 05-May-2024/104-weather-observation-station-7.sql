-- TITLE: WEATHER OBSERVATION STATION 7
-- TASK: Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
-- SOURCE: https://www.hackerrank.com/challenges/weather-observation-station-7
-- 16 May 2024

-- 1st method
SELECT DISTINCT city
FROM station
WHERE city REGEXP '[aiueo]$';

-- 1nd mehtod
SELECT DISTINCT city
FROM station
WHERE city LIKE '%a'
    OR city LIKE '%i'
    OR city LIKE '%u'
    OR city LIKE '%e'
    OR city LIKE '%o';