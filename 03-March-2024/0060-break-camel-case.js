// TITLE: BREAK CAMEL CASE
// TASK : Complete the solution so that the function will break up camel casing, using a space between words.
// Source: https://www.codewars.com/kata/5208f99aee097e6552000148
// 23 March 2024

// 1st method
function solution(string) {
    let newString = '';
    for (let i = 0; i < string.length; i++) {
        if (string.charAt(i) == (string.charAt(i).toUpperCase())) {
            newString += ' '
        }
        newString += string.charAt(i);
    }
    return newString;
}


// Testing
console.log(solution("camelCasing"))