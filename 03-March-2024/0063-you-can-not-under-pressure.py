# TITLE: YOU CAN'T CODE UNDER PRESSURE #1
# TASK : Code as fast as you can! You need to double the integer and return it!
# Source: https://www.codewars.com/kata/53ee5429ba190077850011d4
# 29 March 2024

# 1st method
# def double_integer(i):
#     result = i * 2
#     return result

# 2nd method - lambda function
# double_integer = lambda i: 2 * i

# 3rd method - with a very simple loop 
def double_integer(i):
    result = 0
    for j in range(1, 3):
        result += i
    
    return result
    
# Testing
print(double_integer(4))
print(double_integer(-5))
print(double_integer(-10))
print(double_integer(100))