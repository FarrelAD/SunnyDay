// TITLE: STRING REPEAT
// TASK : Write a function that accepts an integer n and a string s as parameters, 
//        and returns a string of s repeated exactly n times.
// Source: https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
// 9 Febuary 2024

// Function to repeat string
// 1st method
// function repeatStr (n, s) {
//     let result = ''
//     for (let i = 0; i < n; i++) {
//         result += s
//     }
//     return result;
// }

// 2nd method - lambda function
const repeatStr = (n, s) =>  n == 0 ? '' : (s + repeatStr(n - 1, s))

// Testing
console.log(repeatStr(3, "*"))
console.log(repeatStr(8, "ha"))
console.log(repeatStr(5, "Hello"))