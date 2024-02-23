# TITLE: BEGINNER SERIES #1 SCHOOL PAPERWORK
# TASK : Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
#        Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
# Source: https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd
# 23 February 2024

# 1st method
# def paperwork(n, m):
#     if n < 0 or m < 0: 
#         return 0
#     else:
#         return n * m

# 2nd method - using ternary operator
def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n * m

# 3rd method - ONE LINE!!!!!
paperwork = lambda n, m:  0 if n < 0 or m < 0 else n * m

# Testing
print(paperwork(5, 5))
print(paperwork(21, 7))