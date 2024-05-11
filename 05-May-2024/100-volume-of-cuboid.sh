#!/bin/sh

# TITLE: VOLUME OF CUBOID
# TASK: Write a function to calculate the volume of a cuboid with three values: the length, width and height of the cuboid.
# SOURCE: https://www.codewars.com/kata/58261acb22be6e2ed800003a
# 11 May 2024

length=$1
width=$2
height=$3

count_volume() {
    echo "$length * $width * $height" | bc
}

count_volume