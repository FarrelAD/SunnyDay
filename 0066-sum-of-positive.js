// TITLE: SUM OF POSITIVE
// TASK : You get an array of numbers, return the sum of all of the positiveness ones.
// Source: https://www.codewars.com/kata/5715eaedb436cf5606000381
// 03 April 2024

// 1st
// function positiveSum(arr) {
//     result = 0;
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i] > 0) {
//             result += arr[i];
//         }
//     }
//     return result;
// }

// 2nd
const positiveSum = (numbers) => {
    return numbers 
        .map(num => num > 0 ? num : 0)
        .reduce((acc, curr) => acc + curr, 0)
}

// Testing
console.log(positiveSum([1,2,3,4,5]))
console.log(positiveSum([-1,-2,-3,-4,-5]))