// TITLE: PREDICT YOUR AGE
// TASK : In honor of my grandfather's memory we will write a function using his formula!
//        - Take a list of ages when each of your great-grandparent died.
//        - Multiply each number by itself.
//        - Add them all together.
//        - Take the square root of the result.
//        - Divide by two
// Source: https://www.codewars.com/kata/5aff237c578a14752d0035ae
// 13 Oct 2024

import kotlin.math.sqrt

// 1st
// fun predictAge(age1: Int, age2: Int, age3: Int, age4: Int, age5: Int, age6: Int, age7: Int, age8: Int): Int{
//   val ageList = arrayOf(age1, age2, age3, age4, age5, age6, age7, age8)
//   val newAgeList = ageList.map { it * it }
//   val sumAge = newAgeList.reduce { accumulator, number -> accumulator + number }
//   val squareRootSumAge = sumAge.toDouble().let { sqrt(it) }
//   val result = (squareRootSumAge / 2).toInt()
  
//   return result
// }

// 2nd 
fun predictAge(age1: Int, age2: Int, age3: Int, age4: Int, age5: Int, age6: Int, age7: Int, age8: Int): Int{
	return (arrayOf(age1, age2, age3, age4, age5, age6, age7, age8)
        .map { it * it }
			  .reduce { accumulator, number -> accumulator + number }
			  .toDouble().let { sqrt(it) } / 2)
        .toInt()
}

fun main() {
    println(predictAge(65, 60, 75, 55, 60, 63, 64, 45)) // output: 86
}
