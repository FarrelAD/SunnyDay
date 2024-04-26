// TITLE: UNIQUE IN ORDER
// TASK : Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
//        without any elements with the same value next to each other and preserving the original order of elements.
// Source: https://www.codewars.com/kata/54e6533c92449cc251001667
// 28 April 2024

// 1st 
var uniqueInOrder = function(iterable){
    // Variable result is a variable for the real result
    let result = []

    // Looping to check and push to result variable
    for (let i = 0; i < iterable.length; i++) {
        // Add to result array
        if (iterable[i] != result[result.length - 1]) {
            result.push(iterable[i])
        }
    }

    return result
}

// Testing
console.log(uniqueInOrder([1,2,2,3,3]))
console.log(uniqueInOrder('AAAABBBCCDAABBB'))