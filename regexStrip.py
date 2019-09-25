'''Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
to the function will be removed from the string.'''

import re
string = '  test1    test2   test3   '
remove = ''

stripRegex = re.compile(r'\w.*\w+')
removeRegex = re.compile(remove)

def strip(string, *remove):
    if remove == None:
        mo = stripRegex.search(string)
        return mo.group()
    else:
        mo = removeRegex.sub('', string)
        print(mo)

strip(string,)




