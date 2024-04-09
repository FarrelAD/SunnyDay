-- TITLE: QUERY AMERICAN CITIES
-- TASK : Query all columns for all American cities in the CITY table with populations larger than 100000.
--        The CountryCode for America is USA.
-- Source: https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
-- 3 February 2024

-- Below is the SQL code
SELECT * 
FROM CITY
WHERE POPULATION > 100000
AND COUNTRYCODE = 'USA'