// TITLE: STRING ENDS WITH?
// TASK : Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
// Source: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
// 3 May 2024

// 1st
function solution(str, ending) {
    return str.endsWith(ending)
}

// Testing
console.log(solution('abc', 'bc'))
console.log(solution('abcde', 'cde'))
console.log(solution('abcde', 'abc'))


const mystr = 'hbahk'
const str = 'hk'

if (mystr[3] == str) {
    console.log('D')
} else {
    console.log('Apa')
}