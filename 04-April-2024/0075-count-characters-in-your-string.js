// TITLE: COUNT CHARACTERS IN YOUR STRING
// TASK : The main idea is to count all the occurring characters in a string. 
//        If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
// Source: https://www.codewars.com/kata/52efefcbcdf57161d4000091
// 10 April 2024

// 1st
function count(string) {
    let charSet = [];
    for (let i = 0; i < string.length; i++) {
        // Check the character is not already before in 'charSet' array
        let isAlready = false;
        for (let j = 0; j < charSet.length; j++) {
            if (string.charAt(i) == charSet[j]) {
                isAlready = true;
                break;
            }
        }

        // Push unique character to array 'charSet'
        if (!isAlready) {
            charSet.push(string.charAt(i));
        }
    }

    // Create 'resultCount' object as the result of this function
    let resultCount = {};
    for (let i = 0; i < charSet.length; i++) {
        resultCount[charSet[i]] = 0;
    }

    // Count the unique character
    for (let i = 0; i < string.length; i++) {
        for (let j = 0; j < charSet.length; j++) {
            if (string.charAt(i) == charSet[j]) {
                resultCount[charSet[j]] += 1;
            }
        }
    }

    return resultCount;
}


// Testing
console.log(count('aba'))