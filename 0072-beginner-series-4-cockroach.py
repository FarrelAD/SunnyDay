# TITLE: BEGINNER SERIES #4 COCROACH
# TASK : The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and 
#        returns it in cm per second, rounded down to the integer
# Source: https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6
# 08 April 2024

# 1st
# import math

# def cockroach_speed(s):
#     return math.floor(s * 100000 / 3600)

# 2nd
import math

cockroach_speed = lambda s: math.floor(s * 100000 / 3600)

# Testing
print(cockroach_speed(1.08))