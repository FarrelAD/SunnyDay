// TITLE: REMOVING ELEMENTS
// TASK : Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
// Source: https://www.codewars.com/kata/5769b3802ae6f8e4890009d2
// 22 April 2024

// 1st 
// function removeEveryOther(arr) {
//     let result = []
//     for (let i = 0; i < arr.length; i++) {
//         if (i % 2 == 0) {
//             result.push(arr[i])
//         }
//     }
//     return result
// }

// 2nd
// function removeEveryOther(arr) {
//     return arr.filter((value, index) => {
//         if (index % 2 == 0) {
//             return value
//         }
//     })
// }

// 3rd
// const removeEveryOther = (arr) => {
//     return arr.filter((value, index) => index % 2 == 0 ? value : undefined)
// }

// 4th - ONE LINE!
const removeEveryOther = (arr) => arr.filter((value, index) => index % 2 == 0 ? value : undefined)

// Testing
console.log(removeEveryOther(['Hello', 'Goodbye', 'Hello Again']))
console.log(removeEveryOther([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
