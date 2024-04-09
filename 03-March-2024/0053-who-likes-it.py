# TITLE: WHO LIKES IT?
# TASK : Implement the function which takes an array containing the names of people that like an item. 
#        It must return the display text as shown in the examples.
# Source: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
# 7 March 2024

# 1st method
def likes(names):
    like_words = ' like this'
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return names[0] + ' likes this'
    elif len(names) == 2:
        return names[0] + ' and ' + names[1] + like_words
    elif len(names) == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + like_words
    else:
        return names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others' + like_words

# Testing
print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))