// TITLE: ROMAN NUMERALS ENCODER
// TASK : Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and 
//        returning a string containing the Roman Numeral representation of that integer.
// Source: https://www.codewars.com/kata/51b62bf6a9c58071c600001b
// 06 April 2024

public class J_0068_roman_numerals_encoder {
    // 1st
    public static String solution(int n) {
        String result = "";

        if (n / 1000 >= 1) {
            int digit = n / 1000;
            if (digit <= 3) {
                for (int i = 0; i < digit; i++) {
                    result += "M";
                }
            }
            n %= 1000;
        }

        if (n / 100 >= 1) {
            int digit = n / 100;
            if (digit <= 3) {
                for (int i = 0; i < digit; i++) {
                    result += "C";
                }
            } else if (digit <= 8) {
                if (digit == 4) {
                    result += "CD";
                } else {
                    result += "D";
                    for (int i = 0; i < digit - 5; i++) {
                        result += "C";
                    }
                }
            } else {
                result += "CM";
            }

            n %= 100;
        }

        if (n / 10 >= 1) {
            int digit = n / 10;
            if (digit <= 3) {
                for (int i = 0; i < digit; i++) {
                    result += "X";
                }
            } else if (digit <= 8) {
                if (digit == 4) {
                    result += "XL";
                } else {
                    result += "L";
                    for (int i = 0; i < digit - 5; i++) {
                        result += "X";
                    }
                }
            } else {
                result += "XC";
            }

            n %= 10;
        }

        if (n / 1 >= 1) {
            int digit = n / 1;
            if (digit <= 3) {
                for (int i = 0; i < digit; i++) {
                    result += "I";
                }
            } else if (digit <= 8) {
                if (digit == 4) {
                    result += "IV";
                } else {
                    result += "V";
                    for (int i = 0; i < digit - 5; i++) {
                        result += "I";
                    }
                }
            } else {
                result += "IX";
            }

            n %= 10;
        }

        return result;
    }

    public static void main(String[] args) {
        // Testing
        System.out.println(solution(1000)); // M
        System.out.println(solution(1990)); // MCMXC
        System.out.println(solution(1305)); // MCCCV
        System.out.println(solution(1780)); // MDCCLXXX
        System.out.println(solution(1040)); // MXL
        System.out.println(solution(1536)); // MDXXXVI
        System.out.println(solution(3487)); // MMMCDLXXXVII
    }
}