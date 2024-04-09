-- TITLE: QUERY AMERICAN CITIES - 2
-- TASK : Query the NAME field for all American cities in the CITY table with populations larger than 120000. 
--        The CountryCode for America is USA.
-- Source: https://www.hackerrank.com/challenges/revising-the-select-query-2/problem?isFullScreen=true
-- 3 February 2024

-- Below is the SQL code
SELECT NAME 
FROM CITY
WHERE POPULATION > 120000
AND COUNTRYCODE = 'USA'