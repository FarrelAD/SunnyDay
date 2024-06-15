// TITLE: SUM OF TWO LOWEST POSITIVE INTEGER
// TASK : Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
// Source: https://www.codewars.com/kata/558fc85d8fd1938afb000014
// 15 June 2024

function sumTwoSmallestNumbers(numbers) {  
    for (let i = 1; i < numbers.length; i++) {
        const value = numbers[i]
        let j = i;
        while (value < numbers[j -1] && j > 0) {
            numbers[j] = numbers[j - 1]
            j--;
        }
        numbers[j + 1] = value
    }
    
    let firstSmallNum = numbers[0]
    let secondSmallNum = numbers[1]
    return firstSmallNum + secondSmallNum
}

sumTwoSmallestNumbers([5, 8, 12, 19, 22])
sumTwoSmallestNumbers([15, 28, 4, 2, 43])
sumTwoSmallestNumbers([3, 87, 45, 12, 7])