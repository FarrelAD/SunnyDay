// TITLE: SUM OF ARRAYS
// TASK : Write a function that takes an array of numbers and returns the sum of the numbers.
// Source: https://www.codewars.com/kata/53dc54212259ed3d4f00071c
// 28 July 2024

// 1st method
// function sum (numbers) {
//     let result = 0
//     for (const number of numbers) {
//         result += number
//     }
//     return result
// }


// 2nd method
function sum(numbers) {
    if (numbers.length == 0) {
        return 0
    } else {
        return numbers.reduce((accumulator, currentValue) => accumulator + currentValue )
    }
}

// Testing
console.log(sum([1, 5.2, 4, 0, -1]))