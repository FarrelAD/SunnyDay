// TITLE: VOWERL COUNT
// TASK : Return the number (count) of vowels in the given string.
// Source: https://www.codewars.com/kata/54ff3102c1bad923760001f3
// 29 July 2024


// LET'S GO!
// 1st
function getCount(str) {
    let result = 0
    for (let i = 0; i < str.length; i++) {
        if (str[i] == 'a' || str[i] == 'i' || str[i] == 'u' || str[i] == 'e' || str[i] == 'o') {
            result++
        }
    }
    return result
}

// Testing
console.log(getCount('abracadabra'))