# TITLE: BEGINNER - REDUCE BUT GROW
# TASK : Given a non-empty array of integers, return the result of multiplying the values together in order.
# Source: https://www.codewars.com/kata/57f780909f7e8e3183000078
# 10 April 2024

# 1st
# def grow(arr):
#     result = 1
#     for i in arr:
#         result *= i
    
#     return result

# 2nd
from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

# Testing
print(grow([1, 2, 3, 4]))