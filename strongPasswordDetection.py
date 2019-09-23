'''Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength.'''

import re

#TODO: is it at least 8 characters long?

lengthRegex = re.compile(r'(\w){8,}')

#mo_length == None #should be false

#TODO: does it contain both upper

upperRegex = re.compile(r'[A-Z]+')

#TODO: and lowercase characters?

lowerRegex = re.compile(r'[a-z]+')

#TODO: does it have at least one digit?

digitRegex = re.compile(r'\d+')

#TODO: write program to check password

def passwordCheck(pw):
    if lengthRegex.search(pw) == None:
        print('Your password does not have 8 or more characters.')
    elif upperRegex.search(pw) == None:
        print('Your password does not contain an uppercase letter.')
    elif lowerRegex.search(pw) == None:
        print('Your password does not contain a lower case letter.')
    elif digitRegex.search(pw) == None:
        print('Your password does not contain a numeral.')
    else:
        print('Your password is strong.')

print('Enter your passsword:')
pw = input()
passwordCheck(pw)