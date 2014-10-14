'''
Here we'll build a set of functions in order to find the next word in a matrix

placedWords

'''

from lettermatrix import *


def placedWords(oldList, newWord):
    '''
    returns an updated list containing:
        word (string)
        x-coordinate (int)
        y-coordinate (int)
        horizontal (bool)

    oldList::takes in an old list to update
    newWord::takes in the word to add to the list
    '''
    
    newList = oldList
    newList.append(newWord)

    return None


def testWord():
    '''
    Tries to place a given word in the matrix
    First looks for it in the database. If successful, tests the word in the matrix.
    '''


    return None
