# TITLE: SUM WITHOUT HIGHEST AND LOWEST NUMBER
# TASK : Sum all the numbers of a given array except for the highest
#        and lowest element. The highest or lowest element respectively is a single element 
#        at each edge, even if there are more than one with the same value.
# Source: https://www.codewars.com/kata/576b93db1129fcf2200001e6
# 3 February 2024

# Function to get the sum of array
# 1st method - basic function(very long)
# def sum_array(arr):
#     result_sum = 0

#     if arr is not None and len(arr) > 0:
#         highest_num = arr[0]
#         lowest_num = arr[0]

#         # Search highest and lowest value number
#         for i in arr:
#             if i > highest_num:
#                 highest_num = i
#             elif i < lowest_num:
#                 lowest_num = i
        
#         # Change the first highest value of array to 0
#         i = 0
#         while i < len(arr):
#             if arr[i] == highest_num:
#                 arr[i] = 0
#                 break
#             i += 1
        
#         # Change the first lowest value of array to 0
#         i = 0
#         while i < len(arr):
#             if arr[i] == lowest_num:
#                 arr[i] = 0
#                 break
#             i += 1

#         # Sum all the array element value
#         for i in arr:
#             result_sum += i

#     return result_sum

# 2nd method
# def sum_array(arr):
#     result_sum = 0

#     if arr is not None and len(arr) > 0:
#         # Find highest and lowest value
#         highest_num = max(arr)
#         lowest_num = min(arr)

#         # Search for the index of the first highest and lowest value
#         highest_num_index = arr.index(highest_num)
#         lowest_num_index = arr.index(lowest_num)

#         # Remove the first value of the highest and lowest value
#         if arr.count(highest_num) >= 1:
#             arr[highest_num_index] = 0

#         if arr.count(lowest_num) >= 1:
#             arr[lowest_num_index] = 0

#         # Sum all array except the first highest and lowest value
#         result_sum = sum(arr)
    
#     return result_sum

# 3rd method - more short
def sum_array(arr):
    if arr and len(arr) > 1:
        # Find highest and lowest value
        highest_num, lowest_num = max(arr), min(arr)

        # Change value to 0 at the first element of highest and lowest value
        arr[arr.index(highest_num)] = arr[arr.index(lowest_num)] = 0
        return sum(arr)
    return 0

# Testing
print(sum_array(None))
print(sum_array([]))
print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([6, 0, 1, 10, 10]))
print(sum_array([-3, -5]))
