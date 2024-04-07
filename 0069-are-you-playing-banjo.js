// TITLE: ARE YOU PLAYING BANJO?
// TASK : Create a function which answers the question "Are you playing banjo?".
//        If your name starts with the letter "R" or lower case "r", you are playing banjo!
// Source: https://www.codewars.com/kata/53af2b8861023f1d88000832
// 07 April 2024

// 1st
function areYouPlayingBanjo(name) {
    if (name.charAt(0) == 'R' || name.charAt(0) == 'r') {
        return name + " plays banjo"
    } else {
        return name + " does not play banjo"
    }
}

// Testing
console.log(areYouPlayingBanjo('Adam'))
console.log(areYouPlayingBanjo('Ringo'))