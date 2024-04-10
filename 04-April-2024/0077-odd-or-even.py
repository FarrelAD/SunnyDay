# TITLE: ODD OR EVEN?
# TASK : Given a list of integers, determine whether the sum of its elements is odd or even.
# Source: https://www.codewars.com/kata/5949481f86420f59480000e7
# 11 April 2024

# 1st
def odd_or_even(arr):
    sum = 0
    for i in arr:
        sum += i
        
    if sum % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
# 2nd 
# def odd_or_even(arr):
#     sum = 0
#     for i in arr:
#         sum += i
        
#     return 'even' if sum % 2 == 0 else 'odd'

# 3rd
# def odd_or_even(arr):
#     total = sum(arr)
#     return 'even' if total % 2 == 0 else 'odd'

# Testing
print(odd_or_even([0]))
print(odd_or_even([0, 1, 4]))