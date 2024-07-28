# TITLE: CALCULATING WITH FUNCTIONS
# TASK :  Write calculations using functions and get the results.
# Source: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
# 28 July 2024

# LET'S GO!
def zero(data = 0): 
    if data == 0:
        return 0
    
    num = 0
    return calculate_result(num, data)

def one(data = 1): 
    if data == 1:
        return 1
    
    num = 1
    return calculate_result(num, data)

def two(data = 2): 
    if data == 2:
        return 2
    
    num = 2
    return calculate_result(num, data)

def three(data = 3):
    if data == 3:
        return 3
    
    num = 3
    return calculate_result(num, data)


def four(data = 4):
    if data == 4:
        return 4
    
    num = 4
    return calculate_result(num, data)


def five(data = 5): 
    if data == 5:
        return 5
    
    num = 5
    return calculate_result(num, data)

def six(data = 6):
    if data == 6:
        return 6
    
    num = 6
    return calculate_result(num, data)


def seven(data = 7):
    if data == 7:
        return 7
    
    num = 7
    return calculate_result(num, data)

def eight(data = 8):
    if data == 8:
        return 8
    
    num = 8
    return calculate_result(num, data)

def nine(data = 9):
    if data == 9:
        return 9
    
    num = 9
    return calculate_result(num, data)

def plus(num): 
    return 'plus', num

def minus(num):
    return 'minus', num

def times(num):
    return 'times', num
    
def divided_by(num):
    return 'divided_by', num


def calculate_result(num, data):
    result = 0
    if data[0] == 'plus':
        result = num + data[1]
    elif data[0] == 'minus':
        result = num - data[1]
    elif data[0] == 'times':
        result = num * data[1]
    elif data[0] == 'divided_by':
        result = num / data[1]
        
    return int(result)


# Testing
print(seven(times(five()))) # must return 35
print(four(plus(nine()))) # must return 13
print(eight(minus(three()))) # must return 5
print(six(divided_by(two()))) # must return 3