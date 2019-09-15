"""Write a function named printTable() that takes a list of lists of strings and displays it in a
well-organized table with each column right-justified. Assume that all the inner lists will
contain the same number of strings."""
from typing import List

tableData = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    x = max(tableData, key = len)
    longest = max(x, key = len)
    rowWidth = len(longest)
    rows = len(tableData[0])
    z = 0
    while z <= rows:
        for i in range(rows):
            print(tableData[0][z].ljust(rowWidth, ' ') + tableData[1][z].center(rowWidth, ' ') + tableData[2][z].center(rowWidth, ' '))
            z +=1
        break

printTable(tableData)