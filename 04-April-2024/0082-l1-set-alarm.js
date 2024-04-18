// TITLE: L1: SET ALARM
// TASK : The function should return true if you are employed and not on vacation 
//        (because these are the circumstances under which you need to set an alarm). 
//        It should return false otherwise
// Source: https://www.codewars.com/kata/568dcc3c7f12767a62000038
// 18 April 2024

// 1st
// function setAlarm(employed, vacation) {
//     if (employed == true && vacation == false) {
//         return true;
//     } else {
//         return false;
//     }
// }

// 2nd
// function setAlarm(employed, vacation) {
//     return (employed && !vacation)
// }

// 3rd
const setAlarm = (employed, vacation) => employed && !vacation

// Testing
console.log(setAlarm(true, false))