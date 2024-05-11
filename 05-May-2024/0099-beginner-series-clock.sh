#!/bin/sh

# TITLE: BEGINNER SERIES - CLOCK
# TASK: Your task is to write a function which returns the time since midnight in milliseconds.
# SOURCE: https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
# 11 May 2024

h=$1
m=$2
s=$3

result=$(expr $(expr $h \* 3600000) + $(expr $m \* 60000) + $(expr $s \* 1000))

echo $result