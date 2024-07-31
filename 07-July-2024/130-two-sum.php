<?php

// TITLE: TWO SUM
// TASK : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
// Source: https://leetcode.com/problems/two-sum/
// 31 July 2024


// LET'S GO!
// 1st -- ALMOST CORRECT!
// function twoSum($nums, $target) {
//     $additionResult = 0;

//     for ($i=0; $i < count($nums); $i++) { 
//         $additionResult += $nums[$i];

//         if ($additionResult > $target) {
//             return array($i-2, $i-1);
//         } elseif ($additionResult == $target) {
//             return array($i-1, $i);
//         }

//         $additionResult = $nums[$i];
//     }
// }


// 2nd
function twoSum($nums, $target){
    $result = [];
    $gapToTarget = 0;

    for ($i=0; $i < count($nums); $i++) { 
        for ($j=0; $j < count($nums); $j++) { 
            if ($j != $i) {
                $temp = $nums[$i] + $nums[$j];
                $gapToTargetTemp = $target - $temp;
    
                if ($temp == $target) {
                    $result = [$i, $j];
                    break 2;
                } else if ($gapToTargetTemp < $gapToTarget) {
                    $result = [$i, $j];
                }
            }           
        }
    }

    return $result;
}