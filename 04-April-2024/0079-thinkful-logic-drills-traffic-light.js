// TITLE: THINKFUL - LOGIC DRILSS: TRAFFIC LIGHT
// TASK : Complete the function that takes a string as an argument representing the current state of the light and 
//         returns a string representing the state the light should change to.
// Source: https://www.codewars.com/kata/58649884a1659ed6cb000072
// 13 April 2024

// 1st
function updateLight(current) {
    if (current == 'green') {
        return 'yellow'
    } else if (current == 'yellow') {
        return 'red'
    } else if (current == 'red') {
        return 'green'
    }
}

// Testing
console.log(updateLight('green'))
console.log(updateLight('yellow'))
console.log(updateLight('red'))