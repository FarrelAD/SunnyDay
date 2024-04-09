// TITLE: CONVERT BOOLEAN VALUES TO STRINS 'YES' OR 'NO'
// TASK : Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
// Source: https://www.codewars.com/kata/53369039d7ab3ac506000467
// 02 April 2024

// 1.0
// function boolToWord(bool) {
//     if (bool == true) {
//         return 'Yes'
//     } else {
//         return 'No'
//     }
// }

// 2.0
// const boolToWord = function changeItToString(x) {
//     return (x == true) ? 'Yes' : 'No'
// }

// 3.1
// const boolToWord = (x) => {
//     return (x == true) ? 'Yes' : 'No'
// }

// 3.2
const boolToWord = (x) => x ? 'Yes' : 'No'

// Testing
console.log(boolToWord(true))
console.log(boolToWord(false))