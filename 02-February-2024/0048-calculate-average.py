# TITLE: CALCULATE AVERAGE
# TASK : Write a function which calculates the average of the numbers in a given list.
#        Note: Empty arrays should return 0.
# Source: https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
# 29 February 2024

# 1st method
# def find_average(numbers):
#     total = 0
#     for i in numbers: 
#         total += i

#     if len(numbers) == 0:
#         return 0
#     else:
#         return total / len(numbers)
    
# 2nd method
# def find_average(numbers):
#     total = sum(numbers)

#     return 0 if len(numbers) == 0 else total / len(numbers)

# 3rd method - ONE LINE!!
find_average = lambda numbers: 0 if len(numbers) == 0 else sum(numbers) / len(numbers)

# Testing
print(find_average([1, 2, 3]))
print(find_average([]))
print(find_average([5, 7, 3]))