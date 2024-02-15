// TITLE: ARE THEY SAME?
// TASK : Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, 
//        with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in 
//        b are the elements in a squared, regardless of the order.
// Source: https://www.codewars.com/kata/550498447451fbbd7600041c
// 15 Febuary 2024

// Function to detect similarity of two arrays
// 1st method
function comp(array1, array2) {
    if ((array1 == null) || (array2 == null)) {
        return false
    } else {
        if (array1.length != array2.length) {
            return false
        }
    }

    let isArrayOneHavePartner = new Array(array1.length);
    let arrayTwoElementAlreadyChecked = new Array(array2.length);

    for (let i = 0; i < array1.length; i++) {
        isArrayOneHavePartner[i] = false;
    }

    for (let i = 0; i < array1.length; i++) {
        for (let j = 0; j < array2.length; j++) {
            if (!arrayTwoElementAlreadyChecked.includes(j)) {
                if (array1[i] * array1[i] == array2[j]) {
                    isArrayOneHavePartner[i] = true;
                    arrayTwoElementAlreadyChecked[i] = j;
                    break;
                }
            }
        }
    }

    console.log(array1[6] * array1[6]  )

    for (let i = 0; i < isArrayOneHavePartner.length; i++) {
        console.log(isArrayOneHavePartner[i])
        if (isArrayOneHavePartner[i] == false) {
            return false
        }
    }

    return true
}


// Too long? Let's see how AI can simplify my code. (I just copy my code then try them to rewrite it)
// ChatGPT - GPT 3.5
// function comp(array1, array2) {
//     if (!array1 || !array2 || array1.length !== array2.length) {
//         return false;
//     }

//     const sortedSquaredArray1 = array1.map(num => num * num).sort((a, b) => a - b);
//     const sortedArray2 = array2.sort((a, b) => a - b);

//     return sortedSquaredArray1.every((num, index) => num === sortedArray2[index]);
// }

// Google Gemini
// function comp(array1, array2) {
//     // Handle null or different length arrays
//     if (!array1 || !array2 || array1.length !== array2.length) return false;

//     // Use a single set to efficiently store and check paired elements
//     const seen = new Set();

//     // Iterate over the first array
//     for (const num of array1) {
//       const squared = num * num;

//         // Check if the squared value exists in the second array with unique partner
//         if (array2.includes(squared) && !seen.has(squared)) {
//             seen.add(squared);
//         } else {
//             return false;
//         }
//     }

//     return true;
// }
// FAILED!
// The result from Google Gemini is not good. Still many test don't pass in codewars


// Testing
console.log(comp([121, 144, 19, 161, 19, 144, 19, 11],  [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
console.log(comp([121, 144, 19, 161, 19, 144, 19, 11], [231, 14641, 20736, 361, 25921, 361, 20736, 361]))
console.log(comp([121, 144, 19, 161, 19, 144, 19, 11, 1008], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]))
console.log(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]))
console.log(comp([], null))