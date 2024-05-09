// TITLE: LENGTH OF LAST WORD
// TASK : Given a string s consisting of words and spaces, return the length of the last word in the string.
// Source: https://leetcode.com/problems/length-of-last-word
// 9 May 2024


// 1st
using System;
public class Solution {
    public int LengthOfLastWord(string s) {
        string lastWord = "";
        for (int i = s.Length - 1; i >=  0; i--)
        {
            if (s[i] == ' ' && lastWord.Length > 0)
            {
                break;
            }
            else if (s[i] != ' ')
            {
                lastWord += s[i];
            }
        }
        return lastWord.Length;
    }

    // Testing
    static void Main(string[] args) {
        Solution solution = new Solution();
        Console.WriteLine(solution.LengthOfLastWord("Hello World"));
        Console.WriteLine(solution.LengthOfLastWord("luffy is still joyboy"));
    }
}