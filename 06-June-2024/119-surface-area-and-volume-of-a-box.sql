-- TITLE: SURFACE AREA AND VOLUME OF A BOX
-- TASK: Write a function that returns the total surface area and volume of a box as an array: [area, volume]
-- SOURCE: https://www.codewars.com/kata/565f5825379664a26b00007c
-- 07 June 2024

SELECT width, height, depth, (2 * (width * height)) + (2 * (height * depth)) + (2 * (depth * width)) AS area, (width * height * depth) AS volume
FROM box
ORDER BY area, volume, width, height;