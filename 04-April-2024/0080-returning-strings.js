// TITLE: RETURNING STRINGS
// TASK : Make a function that will return a greeting statement that uses an input; 
//        your program should return, "Hello, <name> how are you doing today?"
// Source: https://www.codewars.com/kata/55a70521798b14d4750000a4
// 15 April 2024
// 

// 1st
// function greet(name){
//     return `Hello, ${name} how are you doing today?`
// }

// 2nd
// const greet = function (name) {
//     return `Hello, ${name} how are you doing today?`
// }

// 3rd 
const greet = (name) => `Hello, ${name} how are you doing today?`


// Testing
console.log(greet('Ryan'))
console.log(greet('Alex'))