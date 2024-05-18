#!/bin/bash

# TITLE: MAXIMUM LENGTH DIFFERENCE
# TASK: Fin the maximum length difference of element in the array
# SOURCE: https://www.codewars.com/kata/5663f5305102699bad000056
# 18 May 2024



# input : 2 strings with substrings separated by `,`
# output: number as a string
accum () {
    # Split the input strings into arrays based on comma
    IFS=',' read -ra arr1 <<< "$1"
    IFS=',' read -ra arr2 <<< "$2"

    # Check if either array is empty
    if [ ${#arr1[@]} -eq 0 ] || [ ${#arr2[@]} -eq 0 ]; then
        echo "-1"
        return
    fi

    max_length_diff=-1

    # Calculate the difference in lengths between the array element by iterate each string
    for i in "${arr1[@]}"; do
        for j in "${arr2[@]}"; do
            length_diff=$(expr ${#i} - ${#j})
            abs_length_diff=${length_diff#-}

            if [ $abs_length_diff -gt $max_length_diff ]; then
                max_length_diff=$abs_length_diff
            fi
        done
    done

    echo "$max_length_diff"
}
accum "$1" "$2"