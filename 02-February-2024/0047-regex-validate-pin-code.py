# TITLE: REGEX VALIDATE PIN CODE
# TASK : ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#        If the function is passed a valid PIN string, return true, else return false.
# Source: https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
# 28 February 2024

# 1st method
def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
        else:
            return False
    else:
        return False

# Testing
print(validate_pin('1234'))
print(validate_pin('a123'))