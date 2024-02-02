# TITLE: CONVERT HOURS INTO SECONDS
# TASK : Write a function that converts hours into seconds
# Source: https://edabit.com/challenge/nyeNvKWdDFKRAk4Da
# 2 February 2024

# Function to converts hours into seconds
# 1st method - basic function
# def how_many_seconds(hours):
#     seconds = hours * 60 * 60
#     return seconds

# 2nd method - lambda function
# how_many_seconds = lambda hours : hours * 60 *60 

# 3rd method - using datetime module
from datetime import timedelta

how_many_seconds = lambda hours : int(timedelta(hours=hours).total_seconds())

print(how_many_seconds(2))
print(how_many_seconds(10))
print(how_many_seconds(24))