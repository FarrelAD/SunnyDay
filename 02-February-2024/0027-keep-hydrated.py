# TITLE: KEEP HYDRATED!
# TASK : Nathan loves cycling.Because Nathan knows it is important to stay hydrated, 
#        he drinks 0.5 litres of water per hour of cycling. You get given the time in hours 
#        and you need to return the number of litres Nathan will drink, rounded to the smallest value.
# Source: https://www.codewars.com/kata/582cb0224e56e068d800003c
# 9 February 2024

# Function to get the number litre of Nathan drinks
# 1st  method - using math library
# def litres(time):
#     import math
#     nathan_litres = time / 2
#     return math.floor(nathan_litres)

# 2nd method - lambda function
import math

litres = lambda time : math.floor(time / 2)


# Testing
print(litres(1))
print(litres(1.4))
print(litres(11.8))
print(litres(0.82))
print(litres(12.3))
print(litres(1787))