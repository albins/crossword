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
from array import array
from copy import deepcopy


# a string which will be represented as empty space
EMPTY_CELL = '.'

# a string blocking new words from touching beginning/end of placed words
END_OF_WORD = ','

# enable literal printing of cell characters (for debugging)
DEBUG_PRINT=False

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

    while sizeX > 0:
        column = array('c', EMPTY_CELL * sizeY)   #a row with 0 in each column
        matrix.append(column)
        sizeX -= 1

    return matrix


def printMatrix(matrix):
    '''
    this prints the contents of the matrix in a terminal
    '''

    for column in matrix:
        for cell in column:
            if DEBUG_PRINT:
                print cell,
            elif cell != EMPTY_CELL and cell != END_OF_WORD:
                print cell,
            else:
                print ' ',

        print '\n',

def addWord(word, x, y, hor, m):
    '''
    x :: 0-indexed x-coordinate
    y :: 0-indexed y-coordinate
    hor :: horizontal or not
    word :: word to write
    m :: matrix to test and write

    returns False if it doesn't work, otherwise a new matrix
    '''
    if testNewWord(word,x,y,hor,m) != True:
        return False


    matrix = deepcopy(m)
    i = 0
    j = len(word)


    #write if horizontal
    if hor:
        while i < j:
            matrix[x+i][y] = word[i]
            i += 1

        #adding placeholders
        matrixEdge = len(matrix)
        if x+i != matrixEdge:
            matrix[x+i][y] = END_OF_WORD
        if x != 0:
            matrix[x-1][y] = END_OF_WORD

    #assume it's vertical now
    else:
        while i < j:
            matrix[x][y+i] = word[i]
            i += 1

        #adding placeholders
        matrixEdge = len(matrix[0])
        if y+i != matrixEdge:
            matrix[x][y+i] = END_OF_WORD
        if y != 0:
            matrix[x][y-1] = END_OF_WORD

    return matrix


def testNewWord(word, x, y, hor, matrix):
    i = 0
    j = len(word)



    if x < 0 or y < 0:
        return False

    if hor:
        if x + j > len(matrix):
            return False

        while i < j:
            a = matrix[x+i][y]
            b = word[i]

            #if empty, check surrounding spaces
            if a == EMPTY_CELL:
                #checking above
                if y != 0:
                    above = matrix[x+i][y-1]
                    if above != EMPTY_CELL and above != END_OF_WORD:
                        return False
                #checking beneath
                if y+1 != len(matrix[0]):
                    beneath = matrix[x+i][y+1]
                    if beneath != EMPTY_CELL and beneath != END_OF_WORD:
                        return False

            #else, check if it's the same
            elif a != b:
                return False

            i += 1


        #checking beginning of word
        bow = matrix[x-1][y]
        if bow != EMPTY_CELL and bow != END_OF_WORD and bow != 0:
            return False


        #checking at end of word
        if x+i != len(matrix):
            eow = matrix[x+i][y]
            if eow != EMPTY_CELL and eow != END_OF_WORD:
                return False

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
                if x != 0:
                    left = matrix[x-1][y+i]
                    if left != EMPTY_CELL and left != END_OF_WORD:
                        return False
                #checking to the right
                if x+1 != len(matrix):
                    right = matrix[x+1][y+i]
                    if right != EMPTY_CELL and right != END_OF_WORD:
                        return False

            #else, check if it's the same
            elif a != b:
                return False

            i += 1

        #checking beginning of word
        bow = matrix[x][y-1]
        if bow != EMPTY_CELL and bow != END_OF_WORD and bow != 0:
            return False


        #checking end of word
        if y+i != len(matrix[0]):
            eow = matrix[x][y+i]
            if eow != EMPTY_CELL and eow != END_OF_WORD:
                return False



    #everything looks fine
    return True
