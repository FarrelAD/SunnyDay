// TITLE: FUNCTION 1-HELLO WORLD
// TASK : Make a simple function called greet that returns the most-famous "hello world!".
//        Sure, this is about as easy as it gets. But how clever can you be to create the most creative "hello world" 
//        you can think of? What is a "hello world" solution you would want to show your friends?
// Source: https://www.codewars.com/kata/523b4ff7adca849afe000035
// 01 April 2024

// 1st method
function greet(params) {
    result = '';
    for (let i = 0; i < 12; i++) {
        if (i == 0) {
            result += 'h';
        } else if (i == 1) {
            result += 'e';
        } else if (i == 2 || i == 3 || i == 9) {
            result += 'l';
        } else if (i == 4 || i == 7) {
            result += 'o'
        } else if (i == 5) {
            result += ' ';
        } else if (i == 6) {
            result += 'w';
        } else if (i == 8) {
            result += 'r';
        } else if (i == 10) {
            result += 'd';
        } else if (i == 11) {
            result += '!';
        }
    }

    return result
}


// Testing
console.log(greet())