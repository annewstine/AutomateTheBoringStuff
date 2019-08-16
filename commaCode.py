

#write code to take list as argument, then print it with appropriate separators
def comma(list):
    i = 0
    while True:
        if i < (len(list) - 1):
            print(list[i], ', ', end='')
            i += 1
        else:
            print('and ' + list[-1])
            break

listItems = []
while True:
    print('Enter the list item or enter nothing to stop.')
    list = input()
    if list == '':
        break
    listItems = listItems + [list]

comma(listItems)
