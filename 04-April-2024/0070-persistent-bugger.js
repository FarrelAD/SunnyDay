// TITLE: PERSISTENT BUGGER
// TASK : Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
//        which is the number of times you must multiply the digits in num until you reach a single digit.
// Source: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
// 07 April 2024

// 1st
function persistence(num) {
    let firstTempNum = num;
    let persistence = 0;
    while (firstTempNum >= 10) {
        persistence += 1;
        let tempNum = firstTempNum;
        let arrayNum = getArrayNum(tempNum);
        const multiplication = arrayNum.reduce((accumulator, currentValue) => accumulator * currentValue, 1);
        arrayNum = getArrayNum(multiplication);
        firstTempNum = parseInt(arrayNum.reverse().join(''));
    }
    return persistence;
}

function getArrayNum(num) {
    let tempNum = num;
    let arrayNum = [];
    while (tempNum > 0) {
        const remainder = tempNum % 10;
        arrayNum.push(remainder)
        tempNum = Math.floor(tempNum / 10);
    }
    return arrayNum;
}

// Testing
console.log(persistence(39));
console.log(persistence(999));
console.log(persistence(3471));
console.log(persistence(4));