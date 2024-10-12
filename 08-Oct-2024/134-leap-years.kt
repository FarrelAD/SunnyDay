// TITLE: LEAP YEARS
// TASK : You should simply determine, whether a given year is a leap year or not.
// Source: https://www.codewars.com/kata/526c7363236867513f0005ca
// 12 Oct 2024

fun isLeapYear(year: Int) : Boolean {
    return if (year % 4 == 0 && year % 400 == 0) {
        true
    } else if (year % 4 == 0 && year % 100 == 0) {
        false
    } else if (year % 4 == 0) {
        true
    } else {
        false
    }
}

fun main(args: Array<String>) {
    println(isLeapYear(2004))
}