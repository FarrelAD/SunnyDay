// TITLE: CREATE PHONE NUMBER
// TASK : Write a function that accepts an array of 10 integers (between 0 and 9), 
//        that returns a string of those numbers in the form of a phone number.
// Source: https://www.codewars.com/kata/525f50e3b73515a6db000b83
// 26 Febuary 2024

// 1st method
function createPhoneNumber(numbers){
    let newString = '(';

    for (let i = 0; i < numbers.length; i++) {
        if (i <= 2) {
            newString += numbers[i]
            if (i == 2) newString += ') '
        } else if (i <= 5) {
            newString += numbers[i]
            if (i == 5) newString += '-'
        } else {
            newString += numbers[i]
        }
    }

    return newString;
}

// Testing
console.log(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
console.log(createPhoneNumber([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))