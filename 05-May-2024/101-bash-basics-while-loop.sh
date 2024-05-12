#!/bin/bash

# TITLE: BASH BASICS - WHILE LOOP
# TASK: Create a simple while loop in bash that prints the numbers 1-20 to stdout.
# SOURCE: https://www.codewars.com/kata/582cd9033c1acf1d45000052
# 12 May 2024

countToTwenty() {
    number=1
    while [ $number -le 20 ]
    do
        echo "Count: $number"
        ((number++))
    done
}

countToTwenty