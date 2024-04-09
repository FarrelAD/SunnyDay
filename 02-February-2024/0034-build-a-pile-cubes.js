// TITLE: BUILD A PILE OF CUBES
// TASK : Your task is to construct a building which will be a pile of n cubes.
//        The cube at the bottom eill jave a volume of n^3, the cube above will have volume of (n -1)^3
//        and so on until the top which will have a volume of 1^3. You are given the total volume of the building. 
//        Being given m can you find the number n of cubes you will have to build?
// Source: https://www.codewars.com/kata/5592e3bd57b64d00f3000047
// 16 Febuary 2024

// So, n is the length of the side of the bottom cube.
// 1st method
// function findNb(m) {
//     let powerThreeOfN = 0;
//     let n = 0;
//     do {
//         n++;
//         powerThreeOfN += Math.pow(n, 3);
//     } while (powerThreeOfN < m);

//     if (powerThreeOfN == m) {
//         return n;
//     } else {
//         return -1;
//     }
// }

// 2nd method - make it more clean
function findNb(m) {
    let powerThreeOfN = 0,  n = 0;

    while (powerThreeOfN < m) {
        n++;
        powerThreeOfN += Math.pow(n, 3);
    }

    return powerThreeOfN == m ? n : -1;
}

/////////////////////////////////////////////////// 
// Function to do the reverse step like before I do
function reverseResult(value) {
    if (value == 1) {
        return 1;
    } else {
        return Math.pow(value, 3) + reverseResult(value - 1);
    }
}


// Testing 
console.log(findNb(1071225))
console.log(findNb(91716553919377))
console.log(findNb(135440716410000))
console.log(findNb(225))

// Another testing
console.log(reverseResult(4824))
console.log(reverseResult(45))
console.log(reverseResult(4377))