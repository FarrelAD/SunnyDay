# TITLE: FIND THE ODD INT
# TASK : Given an array of integers, find the one that appears an odd number of times.
#        There will always be only one integer that appears an odd number of times.
# Source: https://www.codewars.com/kata/54da5a58ea159efa38000836
# 12 March 2024

# 1st method
def find_it(seq):
    num_dict = {}
    for i in seq:
        if i not in num_dict:
            num_dict[i] = 1
        else:
            appears = num_dict.get(i) + 1
            num_dict[i] = appears
            
    for key, value in num_dict.items():
        if value % 2 == 1:
            return key


# Testing
print(find_it([0,1,0,1,0]))
print(find_it([1,1,2]))
print(find_it([0]))