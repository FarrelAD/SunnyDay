// TITLE: THE HIGHEST PROFIT WINS!
// TASK : Write a function that returns both the minimum and maximum number of the given list/array.
// Source: https://www.codewars.com/kata/559590633066759614000063
// 12 April 2024

// 1st
function minMax(arr){
    let result = [arr[0], arr[0]];
    for (let i = 0; i < arr.length; i++) {
        const temp = arr[i];
        if (temp > result[1]) {
            result[1] = temp;
        } else if (temp < result[0]) {
            result[0] = temp;
        }
    }
    
    return result;
}

// Testing
console.log(minMax([1, 2, 3, 4, 5]))