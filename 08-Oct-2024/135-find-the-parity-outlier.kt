// TITLE: FIND THE PARITY OUTLIER
// TASK : You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
//        The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
//        Write a method that takes the array as an argument and returns this "outlier" N.
// Source: https://www.codewars.com/kata/5526fc09a1bbd946250002dc
// 13 Oct 2024

// 1st
fun find(integers: Array<Int>): Int {
	val even: ArrayList<Int> = arrayListOf()
  	val odd: ArrayList<Int> = arrayListOf()
    
	for(i in integers) {
        if (i % 2 == 0) even.add(i) else odd.add(i)
    }
    
    return if (even.size == 1) even[0] else odd[0]
}

// Testing
fun main() {
    println(find(arrayOf(2, 4, 0, 100, 4, 11, 2602, 36))) // output: 11
    println(find(arrayOf(160, 3, 1719, 19, 11, 13, -21))) // output: 160
}
