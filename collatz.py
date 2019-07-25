#writing collatz program
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3*number+1

while True:
    print('Enter an integer.')
    try:
        number = int(input())
        while collatz(number) != 1:
            number = collatz(number)
            print(number)
        break
    except ValueError:
        print('That is not an integer.')
        continue







