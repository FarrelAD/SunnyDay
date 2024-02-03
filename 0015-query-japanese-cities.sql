-- TITLE: QUERY JAPANESE CITIES
-- TASK : Query all attributes of every Japanese city in the CITY table. 
--        The COUNTRYCODE for Japan is JPN.
-- Source: https://www.hackerrank.com/challenges/japanese-cities-attributes/problem?isFullScreen=true
-- 3 February 2024

-- Below is the SQL code
SELECT *
FROM CITY
WHERE COUNTRYCODE = 'JPN'