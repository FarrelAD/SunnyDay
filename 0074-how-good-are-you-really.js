// TITLE: HOW GOOD ARE YOU REALLY?
// TASK : There was a test in your class and you passed it. Congratulations!
//        But you're an ambitious person. You want to know if you're better than the average student in your class.
// Source: https://www.codewars.com/kata/5601409514fc93442500010b
// 09 April 2024

// 1st - JavaScript reduce
function betterThanAverage(classPoints, yourPoints) {
    const sumPoints = classPoints.reduce((accum, currValue) => accum + currValue);
    const averagePoint = sumPoints / classPoints.length;
    return yourPoints > averagePoint;
}

// 2nd - for each
// function betterThanAverage(classPoints, yourPoints) {
//     let sum = 0;
//     classPoints.forEach(value => {
//         sum += value
//     });
//     const avgPoint = sum / classPoints.length;
//     return yourPoints > avgPoint;
// }


// Testing
console.log(betterThanAverage([2, 3], 5)) // true
console.log(betterThanAverage([100, 40, 34, 57, 29, 72, 57, 88], 75)) // true
console.log(betterThanAverage([29, 55, 74, 60, 11, 90, 67, 28], 21)) // false