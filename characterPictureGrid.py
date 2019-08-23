#Copy the previous grid value, and write code that uses it to print the image.

#Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0],
# then grid[2][0], and so on, up to grid[8][0].
# This will finish the first row, so then print a newline.
# Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on.
# The last thing your program will print is grid[8][5].

#Also, remember to pass the end keyword argument to print()
# if you don’t want a newline printed automatically after each print() call.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = 0
y = 0
for i in range(len(grid[-1])):
        while y < len(grid[-1]):
                if x < (len(grid)-1):
                        print(grid[x][y], end="")
                        x += 1
                elif x == (len(grid)-1):
                        print(grid[x][y])
                        x += 1
                elif x == len(grid):
                        x = 0
                        y+= 1
                else:
                        break

