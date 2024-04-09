// TITLE: SQUARE EVERY DIGIT
// TASK : In this kata, you are asked to square every digit of a number and concatenate them.
//        For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
//        Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
// Source: https://www.codewars.com/kata/546e2562b03326a88e000020
// 19 February 2024

public class J_0037_square_evry_digit {
    // 1st method
    public int squareDigits(int n) {
        String numInString = Integer.toString(n);
        String result = "";
        int currentNumber;
        for (int i = 0; i < numInString.length(); i++) {
            currentNumber = Integer.parseInt(String.valueOf(numInString.charAt(i)));
            result += Integer.toString((int) Math.pow(currentNumber, 2));
        }

        return Integer.parseInt(result);
    }

    public static void main(String[] args) {
        // Testing
        J_0037_square_evry_digit obj = new J_0037_square_evry_digit();

        System.out.println(obj.squareDigits(345));
        System.out.println(obj.squareDigits(1298));
        System.out.println(obj.squareDigits(9119));
    }
}
