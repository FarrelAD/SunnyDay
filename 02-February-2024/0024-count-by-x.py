# TITLE: COUNT BY X
# TASK : Create a function with two arguments that will return an array of the first n multiples of x.
#        Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Source: https://www.codewars.com/kata/5513795bd3fafb56c200049e
# 7 February 2024

# Function to count x number
# 1st method
def count_by(x, n):
    firstValue = x
    result = []
    i = 0
    while i < n:
        result.append(x)
        x += firstValue
        i += 1
    return result

# Testing
print(count_by(1, 10))
print(count_by(2, 5))
print(count_by(100, 5))