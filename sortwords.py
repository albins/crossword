'''
Here we'll have a few functions for sorting a database of words

weighChar(words)
    takes in a list of words and scores each character
    returns array indexed by letters
    NOTE: only accepts lowercase a-z in ascii

countLetters(words, scoretable)
    receives a word and a scoretable, counts the letters and updates it
    returns new array
    NOTE: only accepts lowercase a-z in ascii

weighWordList(words)
    receives a list of words
    outputs two lists in a list, with words and corresponding scores


weighWord(word, charScore)
    receives a word and general character score
    outputs the score of the word


sortIndexList(scoredWords)
    receives the list with words/score lists, where they share index
    outputs a sorted list of words only


findTopWord(scoredWords)
    receives a words/score list, where they share index
    returns the index of top scoring word
'''

from array import array
baseScore = 120



def weighChar(words):
    '''
    will bring in a list of words and output an array scoring each letter
    '''

    #first we'll make an empty array with 26 slots
    charScore = array('B', [])
    emptyScore = array('B', [baseScore])
    alphabetLength = 26

    for _ in range(0,alphabetLength):
        charScore += emptyScore

    #counts letters and updates charScore for every word in list
    for w in words:
        charScore = countLetters(w, charScore)


    #prints scoretable
    i = 0
    while i < j:
        print charScore[i],
        i += 1

    return charScore


def countLetters(word, nCharScore):
    '''
    count the letters in any in string and update character score
    '''
    for l in word:
        i = ord(l) - 97
        if nCharScore[i] >= 0:
            nCharScore[i] -= 1

    return nCharScore



def weighWordList(words):
    '''
    receives list of strings, counts frequency of characters
    scores words by letting each character add to the score
    '''

    copying received words, otherwise external modifications screw it up
    indexWords = words
    #initializing list wordScore
    wordScore = []

    #generating list of individual character score
    charScore = weighChar(words)

    #generating list of scores for each word, with matching index
    for word in words:
        score = weighWord(word, charScore)
        wordScore.append(score)

    #composing the two lists to a single one
    scoredWords = [indexWords, wordScore]
    return scoredWords



def weighWord(word, charScore):
    '''
    receives a string and a list with scores for each character
    returns the score for the string
    '''

    #initializing score for word
    score = 0

    #finding total by adding the value of each character to score
    for l in word:
        i = ord(l) - 97
        score += charScore[i]
    return score


def sortIndexList(scoredWords):
    '''
    receives a list with a list of words, and a corresponding list of scores
    outputs a list of words, sorted by their score
    '''
    #variables for while-loop
    i = 0
    j = len(scoredWords[1])

    #initializing sorted list for output
    sortedList = []

    #this can probably be deleted..
    index = 0

    while i < j:
        index = findTopWord(scoredWords)
        nextWord = scoredWords[0].pop(index)
        scoredWords[1].pop(index)
        sortedList.append(nextWord)
        i+=1

    return sortedList

def findTopWord(scoredWords):
    '''
    receives a list with list of words and corresponding list of scores
    returns index of the word with highest score
    '''

    topScore = 0
    i = 0
    j = len(scoredWords[1])
    index = 0
    while i < j:
        score = scoredWords[1][i]
        if score > topScore:
            topScore = score
            index = i
        i+=1

    return index




#testing
w = ["hej","hoho","zoo","bu","nationalencyklopedi", "kontroll"]

i = weighWordList(w)
print sortIndexList(i)
