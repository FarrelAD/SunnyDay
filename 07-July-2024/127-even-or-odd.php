<?php

// TITLE: EVEN OR ODD
// TASK : Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
// Source: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
// 30 July 2024

// LET'S GO!
function even_or_odd(int $n): string {
    if ($n % 2 == 0) {
        return "Even";
    } else {
        return 'Odd';
    }
}