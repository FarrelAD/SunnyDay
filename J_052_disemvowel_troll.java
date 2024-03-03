// TITLE: DISEMVOWEL TROLL
// TASK : Trolls are attacking your comment section!
//        A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
//        Your task is to write a function that takes a string and return a new string with all vowels removed.
// Source: https://www.codewars.com/kata/52fba66badcd10859f00097e
// 4 March 2024

public class J_052_disemvowel_troll {
    public static String disemvowel(String str) {
        char[] vowelChar = {'a', 'i', 'u', 'e', 'o'};
        String newString = str;
        for (int i = 0; i < vowelChar.length; i++) {
            newString = newString.replaceAll("(?i)" + vowelChar[i], "");
        }

        return newString;
    }
    public static void main(String[] args) {
        // Testing
        System.out.println(disemvowel("This website is for losers LOL!"));
        System.out.println(disemvowel("No offense but,\n Your writing is among the worst I've ever read"));
    }
}
