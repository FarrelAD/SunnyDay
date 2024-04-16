// TITLE: FIND THE UNIQUE NUMBER
// TASK : There is an array with some numbers. All numbers are equal except for one. Try to find it!
// Source: https://www.codewars.com/kata/5656b6906de340bd1b0000ac
// 16 April 2024

// 1st - using map
function findUniq(arr) {
    // Check all type number and its total
    let numMap = new Map();
    for (let i = 0; i < arr.length; i++) {
        if (!numMap.has(arr[i])) {
            numMap.set(arr[i], 1);
        } else {
            numMap.set(arr[i], numMap.get(arr[i]) + 1);
        }
    }
    
    // Check the key that only contain 1 value
    for (let [key, value] of numMap) {
        if (value == 1) {
            return key
        }
    }
}

// Testing
console.log(findUniq([ 1, 1, 1, 2, 1, 1 ]))
