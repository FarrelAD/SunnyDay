-- TITLE: TYPE OF TRIANGLE
-- TASK: 
--      1. Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical
--      2. Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order
-- SOURCE: https://www.hackerrank.com/challenges/the-pads
-- 19 May 2024


SELECT
    CONCAT(name,'(', LEFT(occupation, 1), ')') AS name
FROM occupations
ORDER BY name ASC;

SELECT
    CONCAT('There are a total of ', COUNT(occupation), ' ', LOWER(occupation), 's.') AS 'total_occupation'
FROM occupations
GROUP BY occupation
ORDER BY COUNT(occupation) ASC, occupation ASC;