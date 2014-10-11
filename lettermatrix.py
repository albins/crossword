'''
This file will contain functions for matrix operations

letterMatrix(int_x, int_y)
    returns a matrix with size x*y

printMatrix(m)
    prints the Matrix m

addWord(int_x, int_y, bool_horizontal, string_word, matrix)
    returns new matrix if successful, otherwise None
'''
#from array import *
#from array import array


# a string which will be represented as empty space
EMPTY_CELL = None

def filter_empty(row_or_column):
    '''
    Filter a row or column from row() or column(), removing empty
    markers.
    '''
    return filter(lambda char: not char == EMPTY_CELL, row_or_column)

def row(m, y):
    '''
    Get the 0-indexed row y from matrix m.
    '''
    return [column[y] for column in m]

def column(m, x):
    '''
    Get the 0-indexed column x from matrix m.
    '''
    return m[x]

def letterMatrix(sizeX, sizeY):
    '''
    we will create a list of arrays, constrained to characters
    '''
    matrix = []         #defining the list

    for _ in range(0, sizeX):
        column = [EMPTY_CELL for __ in range(0, sizeY)]
        matrix.append(column)

    return matrix


def printMatrix(matrix):
    '''
    this prints the contents of the matrix in a terminal
    '''
    for x in range(0, len(matrix)):
        for y in range (0, len(matrix[0])):
            cell = matrix[x][y]
            if cell != EMPTY_CELL:
                print cell,
            else:
                print '.',
        print '' # finishing newline

def addWord(x, y, hor, word, m):
    '''
    x :: 0-indexed x-coordinate
    y :: 0-indexed y-coordinate
    hor :: horizontal or not
    word :: word to write
    m :: matrix to test and write

    returns False if it doesn't work, otherwise a new matrix
    '''
    if testNewWord(x,y,hor,word,m) != True:
        return False


    matrix = m
    i = 0
    j = len(word)


    #write if horizontal
    if hor:
        while i < j:
            matrix[x+i][y] = word[i]
            i += 1

    #assume it's horizontal now
    else:
        while i < j:
            matrix[x][y+i] = word[i]
            i += 1

    return matrix


def testNewWord(x, y, hor, word, matrix):
    i = 0
    j = len(word)

    if hor:
        if x + j > len(matrix):
            return False

        while i < j:
            a = matrix[x+i][y]
            b = word[i]

            #if empty, check surrounding spaces
            if a == EMPTY_CELL:
                #checking above
                if y != 0 and matrix[x+i][y-1] != EMPTY_CELL:
                    return False
                #checking beneath
                if y+1 != len(matrix[0]) and matrix[x+i][y+1] != EMPTY_CELL:
                    return False

            #else, check if it's the same
            elif a != b:
                return False

            i += 1

    #now checking vertical
    else:
        if y + j > len(matrix[0]):
            return False

        while i < j:
            a = matrix[x][y+i]
            b = word[i]

            #if empty, check surrounding spaces
            if a == EMPTY_CELL:
                #checking to the left
                if x != 0 and matrix[x-1][y+i] != EMPTY_CELL:
                    return False
                #checking beneath
                if x+1 != len(matrix) and matrix[x+1][y+i] != EMPTY_CELL:
                    return False

            #else, check if it's the same
            elif a != b:
                return False

            i += 1

    #everything looks fine
    return True
