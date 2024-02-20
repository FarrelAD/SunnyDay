# TITLE: SPLIT STRINGS
# TASK : Complete the solution so that it splits the string into pairs of two characters. 
#        If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
# Source: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
# 20 February 2024

# 1st method
def solution(s):
    splitted_string = []
    temp_string = ''

    for index, char in enumerate(s):
        temp_string += char
        if len(temp_string) == 2:
            splitted_string.append(temp_string)
            temp_string = ''

        if index == len(s) - 1 and len(temp_string) == 1:
            temp_string += '_'
            splitted_string.append(temp_string)
    
    return splitted_string



# Testing
print(solution('abc'))
print(solution('heissogreat'))
print(solution('master'))