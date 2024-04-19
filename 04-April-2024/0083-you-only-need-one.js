// TITLE: YOU ONLY NEED ONE
// TASK : You will be given an array 'a' and a value 'x'. All you need to do is check whether the provided array 
//        contains the value
// Source: https://www.codewars.com/kata/57cc975ed542d3148f00015b
// 19 April 2024

// 1st
// function check(x, y) {
//     for (let i = 0; i < x.length; i++) {
//         if (x[i] == y) {
//             return true;
//         }
//     }
//     return false
// }

const check = (x, y) => x.includes(y)

// Testing
console.log(check([101, 45, 75, 105, 99, 107], 107))
console.log(check(['what', 'a', 'great', 'kata'], 'kat'))