<?php

// TITLE: JADEN CASING STRING
// TASK : Your task is to convert strings to how they would be written by Jaden Smith. 
// Source: https://www.codewars.com/kata/5390bac347d09b7da40006f6
// 30 July 2024


// LET'S GO!
// 1st
function toJadenCase(string $string): string
{
    $result = '';
    for ($i = 0; $i < strlen($string); $i++) {
        if ($i == 0 || $string[$i - 1] == ' ') {
            $result .= strtoupper($string[$i]);
        } else {
            $result .= $string[$i];
        }
    }
    return $result;
}