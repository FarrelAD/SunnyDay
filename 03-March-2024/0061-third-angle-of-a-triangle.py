# TITLE: THIRD ANGLE OF A TRIANGLE
# TASK : You are given two interior angles (in degress) of a triangle. 
#        Write a function to return the 3rd.
# Source: https://www.codewars.com/kata/5a023c426975981341000014
# 24 March 2024

# A triangle must have 180 degrees

# 1st method
# def other_angle(a, b):
#     return 180 - (a + b)

# 2nd method
other_angle = lambda a, b: 180 - (a + b)


# Testing
print(other_angle(30, 60))
print(other_angle(60, 60))
print(other_angle(43, 70))