# TITLE: STRING INCREMENTER
# TASK : Your job is to write a function which increments a string, to create a new string.
#        If the string already ends with a number, the number should be incremented by 1.
#        If the string does not end with a number. the number 1 should be appended to the new string.
# Source: https://www.codewars.com/kata/54a91a4883a7de5d7800009c
# 8 - 10 March 2024

# 1st method
def increment_string(string):
    num_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    
    reversed_string = string[::-1]
    
    number = 0
    num_length = 0
    for iteration, value in enumerate(reversed_string):
        if value not in num_list and iteration > 0:
            if reversed_string[iteration - 1] in num_list:
                index_start = iteration
                number = int(reversed_string[iteration - 1::-1])
                num_length = len(reversed_string[iteration - 1::-1])
                break
        
    index_start = -1
    for i, value in enumerate(string):
        if value not in num_list:
            index_start = i

    number += 1
    new_string = ''
    if index_start != -1:
        new_string += string[:index_start + 1] + str(number).zfill(num_length)
    else:
        if len(string) != 0 and set(list(string)).issubset(set(num_list)):
            string_length = len(string)
            new_string += str(int(string) + 1).zfill(string_length)
        else: 
            new_string += string + str(number).zfill(num_length)
    
    return new_string


# Testing
print(increment_string('foo'))
print(increment_string('foo1'))
print(increment_string('foo099'))
print(increment_string('foobar00999'))
print(increment_string(''))
print(increment_string('00000335319'))
print(increment_string('`2000000107614459'))