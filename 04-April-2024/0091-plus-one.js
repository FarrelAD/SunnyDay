// TITLE: PLUS ONE
// TASK : You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
//        The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's
// Source: https://leetcode.com/problems/plus-one/
// 30 April 2024

// 1st
/**
 * @param {number[]} digits
 * @return {number[]}
 */

var plusOne = function(digits) {
    const n = digits.length;
    
    for (let i = n - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        } else {
            digits[i] = 0;
        }
    }
    
    // The code below only executed when the loop process is done
    digits.unshift(1);
    return digits;
};

// Testing
console.log(plusOne([1,2,3]))
console.log(plusOne([4,3,2,1]))
console.log(plusOne([9]))
console.log(plusOne([6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]))