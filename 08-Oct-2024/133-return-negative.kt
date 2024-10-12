// TITLE: RETURN NEGATIVE
// TASK : In this simple assignment you are given a number and have to make it negative. 
//        But maybe the number is already negative?
// Source: https://www.codewars.com/kata/55685cd7ad70877c23000102
// 12 Oct 2024

class Kata {

    fun makeNegative(x: Int): Int {
        val negativeNumber = if (x <= 0) {
            x
        } else {
            x * -1
        }
        return negativeNumber
    }
}

fun main(args: Array<String>) {
    println(Kata().makeNegative(2))
}