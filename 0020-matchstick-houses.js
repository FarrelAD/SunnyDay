// TITLE: MATCHSTICK HOUSES
// TASK : Create a function that takes a number (step) as an argument 
//        and returns the number of matchsticks in that step
// Source: https://edabit.com/challenge/tYHkTdFrEmWfxpPKF
// 5 February 2024

// Function to find the amount of matchstick
// 1st method - basic function
// function matchHouses(step) {
//     let matchstick = 0
//     if (step > 0) {
//         matchstick = step * 5 + 1
//     }
//     return matchstick
// }

// 2nd method
function matchHouses(step) {
    let matchStick = 0
    if (step > 0) matchStick = step * 5 + 1
    return matchStick
}

// Testing
console.log(matchHouses(1))
console.log(matchHouses(87))
console.log(matchHouses(99))
console.log(matchHouses(0))
console.log(matchHouses(17))