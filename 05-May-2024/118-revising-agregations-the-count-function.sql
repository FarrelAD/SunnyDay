-- TITLE: REVISING AGGREGATIONS - THE COUNT FUNCTION
-- TASK: Query a count of the number of cities in CITY having a Population larger than 100.000.
-- SOURCE: https://www.hackerrank.com/challenges/revising-aggregations-the-count-function
-- 29 May 2024

SELECT COUNT(*)
FROM city
WHERE population > 100000;