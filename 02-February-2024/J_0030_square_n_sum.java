// TITLE: SQUARE(n) SUM
// TASK : Complete the square sum function so that it squares each number passed into it and then sums the results together.
// Source: https://www.codewars.com/kata/515e271a311df0350d00000f
// 12 February 2024

public class J_0030_square_n_sum {
    // 1st method
    // public static int squareSum(int[] n) {
    //     int result = 0;
    //     for (int i = 0; i < n.length; i++) {
    //         result += n[i] * n[i];
    //     }
    //     return result;
    // }

    // 2nd method - using Math.pow
    public static int squareSum(int[] n) {
        int result = 0;
        for (int i = 0; i < n.length; i++) result += Math.pow(n[i], 2);
        return result;
    }

    public static void main(String[] args) {
        // Testing
        int[] myNumbers1 = {1, 2, 3};
        int[] myNumbers2 = {6, 3, 6, 8, 1, 3};
        int[] myNumbers3 = {4, 5, 1, 2, 3, 1, 2, 3};
        int[] myNumbers4 = {1, 2, 2};

        System.out.println(squareSum(myNumbers1));
        System.out.println(squareSum(myNumbers2));
        System.out.println(squareSum(myNumbers3));
        System.out.println(squareSum(myNumbers4));
    }
}