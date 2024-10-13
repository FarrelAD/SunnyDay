// TITLE: SIMPLE BEADS COUNT
// TASK : Implement count_red_beads(n) (in PHP count_red_beads($n); in Java, Javascript, TypeScript, C, C++ countRedBeads(n)) 
//        so that it returns the number of red beads.
//        If there are less than 2 blue beads return 0. 
// Source: https://www.codewars.com/kata/58712dfa5c538b6fc7000569
// 13 Oct 2024

// 1st - normal function
// fun countRedBeads(nBlue: Int): Int {
//     return if (nBlue < 2) 0 else nBlue + nBlue - 2
// }

// 2n - function expression
fun countRedBeads(nBlue: Int): Int = if (nBlue < 2) 0 else nBlue + nBlue - 2

// Testing
fun main() {
    println(countRedBeads(0)) // output: 0
    println(countRedBeads(3)) // output: 4
    println(countRedBeads(5)) // output: 8
    println(countRedBeads(12)) // output: 22
}
