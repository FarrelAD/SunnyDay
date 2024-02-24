# TITLE: FIND MAXIMUM AND MINIMUM VALUES OF A LIST
# TASK : Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) 
#        that receive a list of integers as input, and return the largest and lowest number in that list, respectively.
# Source: https://www.codewars.com/kata/577a98a6ae28071780000989
# 24 February 2024

# 1st method
# def minimum(arr):
#     min_value = 0
#     for index, value in enumerate(arr):
#         if index == 0:
#             min_value = value
#         else:
#             if value < min_value: 
#                 min_value = value
    
#     return min_value


# def maximum(arr):
#     max_value = 0
#     for index, value in enumerate(arr):
#         if index == 0:
#             max_value = value
#         else:
#             if value > max_value: 
#                 max_value = value
    
#     return max_value

# 2nd method
# def minimum(arr):
#     min_value = min(arr)
#     return min_value

# def maximum(arr):
#     max_value = max(arr)
#     return max_value

# 3rd method - more short!
minimum = lambda arr: min(arr)

maximum = lambda arr: max(arr)

# 4th method
# minimum = min
# maximum = max

# Testing
print(minimum([-52, 56, 30, 29, -54, 0, -110]))
print(maximum([-52, 56, 30, 29, -54, 0, -110]))

print(minimum([5]))
print(maximum([5]))

print(minimum([534,43,2,1,3,4,5,5,443,443,555,555]))
print(maximum([534,43,2,1,3,4,5,5,443,443,555,555]))