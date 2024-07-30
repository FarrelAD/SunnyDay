<?php
// TITLE: BASIC MATHEMATHICAL OPERATION
// TASK : Your task is to create a function that does four basic mathematical operations.
// Source: https://www.codewars.com/kata/57356c55867b9b7a60000bd7
// 30 July 2024

// LET'S GO!
// 1st
// function basicOp($op, $val1, $val2)
// {
//     $result = 0;
//     if ($op == '+') {
//         $result = $val1 + $val2;
//     } elseif ($op == '-') {
//         $result = $val1 - $val2;
//     } elseif ($op == '*') {
//         $result = $val1 * $val2;
//     } elseif ($op == '/') {
//         $result = $val1 / $val2;
//     }
//     return $result;
// }

// 2nd
function basicOp($op, $val1, $val2) {
    $result = 0;
    switch ($op) {
        case '+':
            $result = $val1 + $val2;
            break;
        case '-':
            $result = $val1 - $val2;
            break;
        case '*':
            $result = $val1 * $val2;
            break;
        case '/':
            $result = $val1 / $val2;
            break;
        default:
            echo 'something error happen';
            break;
    }
    return $result;
}
?>