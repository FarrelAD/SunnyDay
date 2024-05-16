-- TITLE: WEATHER OBSERVATION STATION 3
-- TASK: Query a list of CITY names from STATION for cities that have an even ID number. 
--      Print the results in any order, but exclude duplicates from the answer.
-- SOURCE: https://www.hackerrank.com/challenges/weather-observation-station-3
-- 16 May 2024

SELECT DISTINCT city 
FROM station
WHERE id % 2 = 0;