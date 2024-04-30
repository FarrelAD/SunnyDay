// TITLE: LIST FILTERING
// TASK : In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
// Source: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
// 30 April 2024

// 1st
function filter_list(l) {
    let result = []
    l.forEach(element => {
        if (Number.isInteger(element)) {
            result.push(element)
        }
    });
    return result
}


// Testing
console.log(filter_list([1,2,'a','b']))
console.log(filter_list([1,2,'aasf','1','123',123]))
console.log(filter_list([1,'a','b',0,15]))