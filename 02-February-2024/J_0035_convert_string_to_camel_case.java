// TITLE: CONVERT STRING TO CAMEL CASE
// TASK : Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
//        The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, 
//        also often referred to as Pascal case). The next words should be always capitalized.
// Source: https://www.codewars.com/kata/517abf86da9663f1d2000003
// 17 February 2024

public class J_0035_convert_string_to_camel_case {
    // 1st method
    static String toCamelCase(String s) {
        String newString = "";
        for (int i = 0; i < s.length(); i++) {
            if (i == 0) {
                newString += (Character.isUpperCase(s.charAt(i))) ? s.charAt(i) : Character.toLowerCase(s.charAt(i));
            } else {
                char currentChar = s.charAt(i), prevChar;
                prevChar = (i == 0) ? '\u0000' : s.charAt(i - 1);

                if (!(currentChar == '_' || currentChar == '-')) {
                    if (prevChar == '-' || prevChar == '_') {
                        newString += Character.toString(currentChar).toUpperCase();
                    } else {
                        newString += currentChar;
                    }
                }
            }
        }
        return newString;
    }

    public static void main(String[] args) {
        // Testing
        System.out.println(toCamelCase("the-stealth-warrior"));
        System.out.println(toCamelCase("The_Stealth_Warrior"));
        System.out.println(toCamelCase("The_Stealth-Warrior"));
    }
}
