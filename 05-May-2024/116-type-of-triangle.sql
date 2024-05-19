-- TITLE: TYPE OF TRIANGLE
-- TASK: Write a query identifying the type of each record in the TRIANGLES table using its three side lengths.
-- SOURCE: https://www.hackerrank.com/challenges/what-type-of-triangle
-- 19 May 2024


-- Wrong query
-- SELECT
--     CASE 
--         WHEN a = b AND b = c THEN 'Equilateral'
--         WHEN a = b OR b = c OR a = c THEN 'Isosceles'
--         WHEN a != b AND b != c THEN 
--             IF(a + b > c  AND + c > b AND b + c > a, 'Scalene', 'Not A Triangle')
--     END AS 'type_of_triangle'
-- FROM triangles;


-- Correct query
SELECT
    CASE 
        WHEN a + b <= c OR a + c <= b OR b + c <= a THEN 'Not A Triangle'
        WHEN a = b AND b = c THEN 'Equilateral'
        WHEN a = b OR b = c OR a = c THEN 'Isosceles'
        ELSE 'Scalene'
    END AS type_of_triangle
FROM triangles;

