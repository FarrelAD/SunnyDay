// TITLE: IS A NUMBER PRIME?
// TASK : Define a function that takes an integer argument and returns a logical value true or false 
//        depending on if the integer is a prime.
// Source: https://www.codewars.com/kata/5262119038c0985a5b00029
// 18 February 2024

import java.util.ArrayList;

public class J_0036_is_a_number_prime {
    // 1st method - FAIL [!]
    // public static boolean isPrime(int num) {
    //     if (num <= 1) {
    //         return false;
    //     } else {
    //         ArrayList<Boolean> isNumberCanDivided = new ArrayList<>();
    //         // Check the factor of the number
    //         for (int i = 1; i <= 3 || i == 5 || i == 7; i++) {
    //             if (num % i == 0) {
    //                 isNumberCanDivided.add(true);
    //             }
    //         }

    //         if (num == 4 || num == 6 || num > 7) {
    //             isNumberCanDivided.add(num % num == 0 ? true : false);
    //         }

    //         // Count the amount of true elements
    //         int amountOfTrueElements = 0;
    //         for (Boolean element : isNumberCanDivided) {
    //             if (element == true) {
    //                 amountOfTrueElements++;
    //             }
    //         }

    //         if (amountOfTrueElements > 2) {
    //             return false;
    //         } else {
    //             return true;
    //         }
    //     }
    // }

    // 2nd method
    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        if (num <= 3) {
            return true;
        }
        if (num % 2 == 0 || num % 3 == 0) {
            return false;
        }
        // Prime numbers are of the form 6k ± 1
        for (int i = 5; i * i <= num; i += 6) {
            if (num % i == 0 || num % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        // Testing
        System.out.println(isPrime(2)); // true
        System.out.println(isPrime(3)); // true
        System.out.println(isPrime(1)); // false
        System.out.println(isPrime(-3)); // false
        System.out.println(isPrime(4)); // false
        System.out.println(isPrime(89)); // true
        System.out.println(isPrime(41)); // true
        System.out.println(isPrime(79)); // true
        System.out.println(isPrime(63)); // false
        System.out.println(isPrime(911591157));
        System.out.println(isPrime(1775363371));

        // if (num % 5 == 0) {
        //     isNumberCanDivided[3] = true;
        // }

        // if (num % 7 == 0) {
        //     isNumberCanDivided[4] = true;
        // }

        // if (num > 7) {
        //     if (num % num == 0) {
        //         isNumberCanDivided[5] = true;
        //     }
        // }
    }
}
