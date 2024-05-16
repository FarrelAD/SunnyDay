-- TITLE: WEATHER OBSERVATION STATION 8
-- TASK: Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
-- SOURCE: https://www.hackerrank.com/challenges/weather-observation-station-8
-- 16 May 2024

-- 1st method
SELECT DISTINCT city
FROM station
WHERE (city LIKE 'a%' AND city LIKE '%a')
    OR (city LIKE 'a%' AND city LIKE '%i')
    OR (city LIKE 'a%' AND city LIKE '%u')
    OR (city LIKE 'a%' AND city LIKE '%e')
    OR (city LIKE 'a%' AND city LIKE '%o')
    OR (city LIKE 'i%' AND city LIKE '%a')
    OR (city LIKE 'i%' AND city LIKE '%i')
    OR (city LIKE 'i%' AND city LIKE '%u')
    OR (city LIKE 'i%' AND city LIKE '%e')
    OR (city LIKE 'i%' AND city LIKE '%o')
    OR (city LIKE 'u%' AND city LIKE '%a')
    OR (city LIKE 'u%' AND city LIKE '%i')
    OR (city LIKE 'u%' AND city LIKE '%u')
    OR (city LIKE 'u%' AND city LIKE '%e')
    OR (city LIKE 'u%' AND city LIKE '%o')
    OR (city LIKE 'e%' AND city LIKE '%a')
    OR (city LIKE 'e%' AND city LIKE '%i')
    OR (city LIKE 'e%' AND city LIKE '%u')
    OR (city LIKE 'e%' AND city LIKE '%e')
    OR (city LIKE 'e%' AND city LIKE '%o')
    OR (city LIKE 'o%' AND city LIKE '%a')
    OR (city LIKE 'o%' AND city LIKE '%i')
    OR (city LIKE 'o%' AND city LIKE '%u')
    OR (city LIKE 'o%' AND city LIKE '%e')
    OR (city LIKE 'o%' AND city LIKE '%o');

-- 2nd method
SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[aeiou].*[aeiou]$';