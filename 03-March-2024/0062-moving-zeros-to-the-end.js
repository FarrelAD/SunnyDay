// TITLE: MOVING ZEROS TO THE END
// TASK : Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
// Source: https://www.codewars.com/kata/52597aa56021e91c93000cb0
// 25 March 2024

// 1st method
function moveZeros(arr) {
    for (let i = arr.length - 1; i >= 0; i--) {
        if (arr[i] === 0) {
            arr.push(arr[i]);
            arr.splice(i, 1);
        }
    }
    return arr;
}

// Testing
console.log(moveZeros([false,1,0,1,2,0,1,3,"a"]))
console.log(moveZeros([ 9, +0, 9, 1, 2, 1, 1, 3, 1, 9, +0, +0, 9, +0, +0, +0, +0, +0, +0, +0 ]))