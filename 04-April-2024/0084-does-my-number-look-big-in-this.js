// TITLE: DOES MY NUMBER LOOK BIG IN THIS?
// TASK : Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.
// Source: https://www.codewars.com/kata/5287e858c6b5a9678200083c
// 20 April 2024


// 1st
// function narcissistic(value) {
//     const stringNum = value.toString()
//     const digitLength = stringNum.length
//     let result = 0
//     for (let i = 0; i < digitLength; i++) {
//         let power = digitLength
//         let resultPower = 1
//         while (power > 0) {
//             resultPower *= parseInt(stringNum[i], 10)
//             power--
//         }
//         result += resultPower
//     }
    
//     if (result == value) {
//         return true
//     } else {
//         return false
//     }
// }

// 2nd
const narcissistic = (value) => {
    const arrayNum = value.toString().split('').map(Number)
    const sumOfPower = arrayNum.reduce((accumulator, currentValue) => accumulator + Math.pow(currentValue, arrayNum.length), 0)
    return sumOfPower == value
}

// Testing
console.log(narcissistic(153))
console.log(narcissistic(40028394225))
