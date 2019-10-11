#! python3
# Creates a Mad Libs program that reads in text files and lets the user add
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
# appears in the text file.

import re

def madLibs(ADJECTIVE, NOUN, VERB, NOUN2):
    # TODO: write and open starter text file
    madLibsFile = open('madLibs.txt', 'w')
    madLibsFile.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
    madLibsFile.close()
    madLibsFile = open('madLibs.txt')
    content = madLibsFile.read()
    madLibsFile.close()
    #print(content)  #use this line to test

    # TODO: Substitute user text for words in text file and print
    NOUNregex = re.compile(r'NOUN')
    newContent = NOUNregex.sub(NOUN, content, 1)
    ADJregex = re.compile(r'ADJECTIVE?')
    newContent = ADJregex.sub(ADJECTIVE, newContent, 1)
    VERBregex = re.compile(r'VERB?')
    newContent = VERBregex.sub(VERB, newContent, 1)
    newContent = NOUNregex.sub(NOUN2, newContent, 1)
    print(newContent)

    # TODO: Save output as text file
    outputFile = open('madLibsOutput.txt', 'w')
    outputFile.write(newContent)
    outputFile.close()

#Collect user input
print('Enter an ADJECTIVE.')
ADJECTIVE = input()

print('Enter a NOUN.')
NOUN = input()

print('Enter a VERB.')
VERB = input()

print('Enter another NOUN.')
NOUN2 = input()

#Run the program based on user input
madLibs(ADJECTIVE, NOUN, VERB, NOUN2)



