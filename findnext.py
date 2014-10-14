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
        print tryNewWord
        #if it works, delete it from its list and return a new list using the added word
        if tryNewWord != False:
            newWords.pop(index)
            #return placedWords.append(tryNewWord)
            print "now?"
            return tryNewWord 
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
            print placedChar,
            #now we compare that character to those in the new word
            testCharIndex = 0
            for testChar in testWord:
                print testChar,
                #if they're the same, we try if it fits in the matrix
                if testChar == placedChar:
                    x = placedWords[1][index]
                    y = placedWords[2][index]
                    hor = True
                    
                    #shifting x/y/hor values according to horizontal
                    #...and where the character is
                    if placedWords[3][index] == True:
                        hor = False
                        x += placedCharIndex
                        y -= testCharIndex
                        print "vertical"
                        print x, y
                    else:
                        hor = True
                        y += placedCharIndex
                        x -= testCharIndex

                    #now trying to place the character in the matrix
                    if testNewWord(x,y,hor,testWord,matrix) != False:
                        print "returning the word"
                        return [testWord, x, y, hor]
                    
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






'''
a couple of test runs
'''


w0 = ["aoeu","oeui","euid","uidh"]
w1 = [2, 3, 5, 6]
w2 = [2, 9, 2, 9]
w3 = [True, True, True, True]
w = [w0,w1,w2,w3]
print w
m1 = letterMatrix(20,20)
m1 = addWord(w[1][0],w[2][0],w[3][0],w[0][0],m1)
printMatrix(m1)
print "now testing testWord"
#t1 = testWord(m1, w, "oooo")
#print t1
nw0 = ["xx", "cool"]
nw = placeNextWord(m1, w, nw0)
print nw
m2 = addWord(nw[1],nw[2],nw[3],nw[0],m1)
printMatrix(m2) 



