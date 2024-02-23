# TITLE: OPPSOITE NUMBER
# TASK : Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).
# Source: https://www.codewars.com/kata/56dec885c54a926dcd001095
# 24 February 2024

# 1st method
# def opposite(number):
#     number = number * (-1)
#     return number

# 2nd method
# def opposite(number):
#     return number * (-1)

# 3rd method - lamnda function
opposite = lambda number: number * (-1)

# Testing
print(opposite(-78))
print(opposite(34))