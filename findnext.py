'''
Here we'll build a set of functions in order to find the next word in a matrix

placedWords

'''

from lettermatrix import *


def placeNextWord(matrix, placedWords, newWords):
    '''
    returns an updated list containing:
        word (string)
        x-coordinate (int)
        y-coordinate (int)
        horizontal (bool)

    placedWords :: takes in an old list to update
    newWords :: takes in new words to try and add to the list
    if no new word was found, return False


    note that the matrix must contain AT LEAST one word
    '''
    index = 0
    #pick a new word to try
    for newWord in newWords:
        
        #test the word by using a new variable
        tryNewWord = testWord(matrix, placedWords, newWord)

        #if it works, delete it from its list and return a new list using the added word
        if testWord(matrix, placedWords, newWord) != False:
            newWords.pop([index])
            return placedWords.append(tryNewWord)
        
        index += 1

    #if none of the new words fit, return False
    return False


def testWord(matrix, placedWords, testWord):
    '''
    Tries to place a given word in the matrix
    First looks for it in the database. If successful, tests the word in the matrix.
    
    If word can be placed, it will output a list of word, x, y 
    '''

    #first we pick a word from list of used words
    index = 0
    for placedWord in placedWords[0]:

        #then we pick a character from a placed word
        placedCharIndex = 0
        for placedChar in placedWord:

            #now we compare that character to those in the new word
            testCharIndex = 0
            for testChar in testWord:

                #if they're the same, we try if it fits in the matrix
                if testChar == char:
                    x = placedWord[1][i]
                    y = placedWord[2][i]

                    #the new word must cross the placed word
                    hor != placedWord[3][i]

                    #shifting x/y values according to where the character is
                    if hor != True:
                        x += placedCharIndex
                        y -= testCharIndex
                    else:
                        y += placedCharIndex
                        x -= testCharIndex

                    #now trying to place the character in the matrix
                    if testNewWord(x,y,hor,testWord,matrix) != False:
                        return [word, x, y, hor]
                    
                testCharIndex += 1
            placedCharIndex += 1
        index += 1
    return False

def findMiddle(m, word):
    # FIXME: actually calculate middle
    xsize = len(m)
    ysize = len(m[0])
    if xsize % 2 == 1:
        xsize += 1
        xmiddle = xsize / 2
    else:
        xmiddle = xsize / 2

    if ysize % 2 == 1:
        ysize += 1
        ymiddle = ysize / 2
    else:
        ymiddle = ysize / 2

    #this finds starting point for new word
    if len(word) % 2 == 1:
        xmiddle -= (len(word)+1) / 2
    else:
        xmiddle -= len(word) / 2

    return [xmiddle, ymiddle]

def stupidlyPlaceWord(m, word):
    return None

def stupidlyPlaceWords(m, words):
    x, y = findMiddle(m, words[0])
    # first word is always horizontal
    m = addWord(x, y, True, words[0])

    # add the rest of the words
    for word in words[1:]:
        # try to place a word
        # if it succeeded, proceed
        # otherwise bail out, returning results so far
        break
