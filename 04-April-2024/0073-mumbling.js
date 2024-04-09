// TITLE: MUMBLING
// TASK : Do like this:
//        1. accum("abcd") -> "A-Bb-Ccc-Dddd"
//        2. accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
//        3. accum("cwAt") -> "C-Ww-Aaa-Tttt"
// Source: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
// 08 April 2024

// 1st
function accum(s) {
    const newString = s.toLowerCase();
    let result = '';
    for (let i = 0; i < newString.length; i++) {
        for (let j = 1; j <= i + 1; j++) {
            if (j == 1) {
                result += newString.charAt(i).toUpperCase();
            } else {
                result += newString.charAt(i);
            }

            if (j == i+1 && i != s.length - 1) {
                result += '-'
            }
        }
    }

    return result
}

// Testing
console.log(accum('abcd'))
console.log(accum('ZpglnRxqenU'))