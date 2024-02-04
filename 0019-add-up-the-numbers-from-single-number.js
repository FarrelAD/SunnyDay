// TITLE: ADD UP THE NUMBERS FROM A SINGLE NUMBER
// TASK : Add up all the numbers from 1 to the number you passed to the function. 
//        For example, if the input is 4 then your function should return 
//        10 because 1 + 2 + 3 + 4 = 10.
// Source: https://edabit.com/challenge/4gzDuDkompAqujpRi
// 4 February 2024

// Function to add up the numbers
// 1st method
// function addUp(num) {
//     let result_sum = 0;
//     for (let i = 1; i <= num; i++) {
//         result_sum += i;
//     }
//     return result_sum;
// }

// 2nd method - recursion functiion
// function addUp(num) {
//     if (num == 0) {
//         return 0
//     } else {
//         return (num + addUp(num - 1))
//     }
// }

// 3rd method - ONE LINER!!
const addUp = num => num === 0 ? 0 : (num + addUp(num - 1));

console.log(addUp(4))
console.log(addUp(925))
console.log(addUp(53))