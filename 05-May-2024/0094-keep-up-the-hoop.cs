// TITLE: KEEP UP THE HOOP
// TASK : Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message :)
// Source: https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145
// 7 May 2024

public class Kata
{
    public static string HoopCount(int n)
    {
        if (n >= 10)
        {
            return "Great, now move on to tricks";
        }
        else
        {
            return "Keep at it until you get it";
        }
    }
}