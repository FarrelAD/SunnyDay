// TITLE: REVERSED STRINGS
// TASK : Complete the solution so that it reverses the string passed into it.
// Source: https://www.codewars.com/kata/5168bb5dfe9a00b126000018
// 13 February 2024

public class J_0031_reversed_strings {
    // 1st method
    // public static String solution(String str) {
    //     String newString = "";

    //     for (int i = (str.length() - 1); i >= 0; i--) {
    //         newString += str.charAt(i);
    //     }

    //     return newString;
    // }

    // 2nd method - use string builder
    // public static String solution(String str) {
    //     String newString = new StringBuilder(str).reverse().toString();
    //     return newString;
    // }

    // 3rd method - MORE SHORT
    // public static String solution(String str) {
    //     return new StringBuilder(str).reverse().toString();
    // }

    // 4th method - ONE LINE!
    public static String solution(String str) { return new StringBuilder(str).reverse().toString();}

    public static void main(String[] args) {
        System.out.println(solution("world"));
        System.out.println(solution("responsibilities"));

    }
}