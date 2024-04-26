-- TITLE: COMBINE TWO TABLES
-- TYPE: SQL, DATABASE
-- TASK: Write a solution to report the first name, last name, city, and state of each person in the Person table. 
--       If the address of a personId is not present in the Address table, report null instead.
--       Return the result table in any order.
-- SOURCE: https://leetcode.com/problems/combine-two-tables
-- 26 April 2024


# Write your MySQL query statement below

SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId