<?php

// TITLE: CONVERT BOOLEAN TO STRING
// TASK : Implement a function which convert the given boolean value into its string representation.
// Source: https://www.codewars.com/kata/551b4501ac0447318f0009cd
// 30 July 2024

// LET'S GO!
// 1st - almost correct
// function booleanToString($b) {
//     return (string) $b;
// }


// 2nd
function booleanToString($b) {
    return $b ? 'true' : 'false';
}