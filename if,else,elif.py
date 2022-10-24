import re

user_input = input("Choose a password:")


def valid_password(password):
    is_valid = True
# if - will go over all the code and whatever is false will return the print
# elif - will go over the code only if the statement before doesn't return
    if len(password) < 8:
        print("password must be at least 8 char long")
        is_valid = False
    if re.search('[0-9]', password) is None:
        print('password must contain at least one number')
        is_valid = False
    if re.search('[a-z]', password) is None:
        print('password must contain at least one letter')
        is_valid = False

    if (is_valid):
        print('OK')
    else:
        print('Not Valid!')

    return is_valid


this_is_valid = valid_password(user_input)
print('result:', this_is_valid)
