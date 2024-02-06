// TITLE: RETURN THE TIME SAVED BY SPEEDING
// TASK : Create a function that calculates the amount of time saved were you traveling with an average speed 
//        that is above the speed-limit as compared to traveling with an average speed exactly at the speed-limit. 
// Source: https://edabit.com/challenge/fkzJMioMcnP4p4BFG
// 6 February 2024

// Function to count the time saved by speeding
// 1st method - basic function
// function timeSaved(lim, avg, d) {
//     const slowMilePerMinutes = 60 / lim
//     const speedingMilePerMinutes = 60 / avg
//     const slowTime = slowMilePerMinutes * d
//     const speedingTime = speedingMilePerMinutes * d
//     const timeDifference = slowTime - speedingTime
//     return Math.round(timeDifference * 10) / 10
// }

// 2nd method 
// function timeSaved(lim, avg, d) {
//     const firstTime = 60 / lim * d
//     const speedingTime = 60 / avg * d
//     const timeDifference = firstTime - speedingTime
//     return Math.round(timeDifference * 10) / 10
// }

// 3rd method
// function timeSaved(lim, avg, d) {
//     return Math.round(((60 / lim * d) - (60 / avg * d)) * 10) / 10
// }

// 4th method - ONE LINER
const timeSaved = (lim, avg, d) => Math.round(((60 / lim * d) - (60 / avg * d)) * 10) / 10
// Testing
console.log(timeSaved(80, 90, 40))
console.log(timeSaved(80, 100, 40))
console.log(timeSaved(80, 90, 4000))