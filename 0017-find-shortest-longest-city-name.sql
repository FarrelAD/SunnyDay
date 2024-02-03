-- TITLE: FIND THE SHORTEST AND LONGEST CITY NAME
-- TASK : Query the two cities in STATION with the shortest and longest CITY names, 
--        as well as their respective lengths (i.e.: number of characters in the name). 
--        If there is more than one smallest or largest city, choose the one that comes first 
--        when ordered alphabetically.
-- Source: https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
-- 3 February 2024

-- Below is the SQL code
-- 1st method
SELECT CITY, LENGTH(CITY)
FROM STATION
WHERE LENGTH(CITY) = (SELECT MIN(LENGTH(CITY)) FROM STATION)
ORDER BY CITY LIMIT 1;

SELECT CITY, LENGTH(CITY)
FROM STATION
WHERE LENGTH(CITY) = (SELECT MAX(LENGTH(CITY)) FROM STATION)
ORDER BY CITY LIMIT 1;

-- 2nd method
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) ASC, CITY ASC
LIMIT 1;

-- City with the maximum length
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY ASC
LIMIT 1;