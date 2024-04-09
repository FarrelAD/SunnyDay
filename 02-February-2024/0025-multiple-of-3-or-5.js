// TITLE: TEMPERATURE CONVERSION
// TASK : If we list all the natural number below 10 that are multiple of 3 or 5, we get 3, 5, 6, and 9.
//        The sum of these multiple is 23. Finish the solution so that it returns the sum of all the multiples 3 or 5 below 
//        the number passed in.
// Source: https://www.codewars.com/kata/514b92a657cdc65150000006
// 8 Febuary 2024

// Function to find the sum of multiple 3 or 5
// 1st method
function solution(number){
    let result = 0
    for (let i = 1; i < number; i++) {
        if ((i % 3 == 0) || (i % 5 == 0)) {
            result += i
        }
    }
    return result
}


// Testing
console.log(solution(10))
console.log(solution(50))
console.log(solution(125))
console.log(solution(-25))