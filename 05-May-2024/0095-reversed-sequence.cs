// TITLE: REVERSED SEQUENCE
// TASK : Build a function that returns an array of integers from n to 1 where n>0.
// Source: https://www.codewars.com/kata/5a00e05cc374cb34d100000d
// 8 May 2024

// 1st
using System;
using System.Collections.Generic;

public static class Kata
{
    public static int[] ReverseSeq(int n)
    {
        List<int> result = new List<int>();
        for (int i = n; i > 0; i--)
        {
            result.Add(i);
        }
        return result.ToArray();
    }
}