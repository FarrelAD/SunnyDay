// TITLE: ISOGRAMS
// TASK : An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
//        Implement a function that determines whether a string that contains only letters is an isogram
// Source: https://www.codewars.com/kata/54ba84be607a92aa900000f1
// 11 March 2024

public class J_0056_isograms {
    public static boolean  isIsogram(String str) {
        String newStr = str.toLowerCase();
        char allChar[] = new char[newStr.length()];
        
        for (int i = 0; i < newStr.length(); i++) {
            // Checking the avaiibility of the character before
            for (int j = 0; j < allChar.length; j++) {
                char temp = allChar[j];
                if (newStr.charAt(i) == temp) {
                    return false;
                }
            }
            allChar[i] = newStr.charAt(i);
        }

        return true;
    } 

    public static void main(String[] args) {
        // Testing
        System.out.println(isIsogram("moose"));
        System.out.println(isIsogram("Dermatoglyphics"));
        System.out.println(isIsogram("thumbscrewjapingly"));
        System.out.println(isIsogram(""));
        System.out.println(isIsogram("moOse"));
        System.out.println(isIsogram("aba"));
    }
}