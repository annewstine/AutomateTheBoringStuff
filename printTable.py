"""Write a function named printTable() that takes a list of lists of strings and displays it in a
well-organized table with each column right-justified. Assume that all the inner lists will
contain the same number of strings."""

tableData = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    #columns = len(tableData)
    # rows = len(tableData[0])
    x = max(tableData, key = len)
    longest = max(x, key = len)
    global rowWidth
    rowWidth = len(longest)

    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(tableData[x][y].rjust(rowWidth, ' '), end=' ')
        print()

printTable(tableData)
