// TITLE: SUMMING A SLICE
// TASK : Given an array and an integer n, 
//        return the sum of the first n numbers in the array.
// Source: https://edabit.com/challenge/B3FR3P7g8NyTg7t8b
// 1 February 2024

// Function to return the sum of the first n numbers in the array
// 1st method - basic function
// function sliceSum(arr, n) {
//     let sum = 0;
    
//     if (n > arr.length) {
//         n = arr.length
//     }

//     for (let i = 0; i < n; i++) {
//         sum += arr[i];
//     }
//     return sum;
// }

// 2nd - method - shorter method than the first method
// function sliceSum(arr, n) {
//     let sum = 0;
//     let x = n > arr.length ? n = arr.length : n
//     for (let i = 0; i < x; i++) sum += arr[i];
//     return sum;
// }

// 3rd - method - one liner
// const sliceSum = (arr, n) => {let sum = 0; if (n > arr.length) n = arr.length; for (let i = 0; i < n; i++) sum += arr[i]; return sum}

// 4th - method - another one liner
const sliceSum = (arr, n) => arr.slice(0, n).reduce((sum, val) => sum + val, 0);

console.log(sliceSum([1, 3, 2], 2))
console.log(sliceSum([4, 2, 5, 7], 4))
console.log(sliceSum([3, 6, 2], 0))
console.log(sliceSum([2, 4], 9))