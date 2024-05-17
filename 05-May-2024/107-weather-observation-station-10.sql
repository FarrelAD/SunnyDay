-- TITLE: WEATHER OBSERVATION STATION 10
-- TASK: Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
-- SOURCE: https://www.hackerrank.com/challenges/weather-observation-station-10
-- 17 May 2024

-- 1st method
SELECT DISTINCT city
FROM station
WHERE city NOT LIKE '%a'
    AND city NOT LIKE '%i'
    AND city NOT LIKE '%u'
    AND city NOT LIKE '%e'
    AND city NOT LIKE '%o';


-- 2nd method
SELECT DISTINCT city
FROM station
WHERE city NOT REGEXP '[aiueo]$';