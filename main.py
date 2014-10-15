#!/usr/bin/env python2
import argparse
import lettermatrix as matrix
import findnext as solver
import sortwords as sort

def sanitizeWords(words):
    '''
    Clean a list of words from all non-lower-case ASCII letters.
    '''
    def sanitizeWord(word):
        start = ord('A')
        end = ord('z') + 1
        asciiWord = ''.join([i  if ord(i) in range(start, end) else '' for i in word])
        return asciiWord.lower()

    return map(sanitizeWord, words)



def recursivePlaceWords(m, placedWords, newWords):

    newWord = solver.placeNextWord(m, placedWords, newWords)

    #if it's possible to place
    if newWord != False:
        #put it in a matrix and add it to list of placed words
        m = matrix.addWord(newWord[1],newWord[2],newWord[3],newWord[0], m)
        placedWords.append(newWord)

        #remove it from list of new words. would be nice to find a better solution.
        index = 0
        for word in newWords:
            if word == newWord[0]:
                newWords.pop(index)
            index += 1

        #call function again
        m = recursivePlaceWords(m, placedWords, newWords)

    return m

def main(size, words):
    cleanWords = sort.sortWords(sanitizeWords(words))
    #initialize new words and list of placed words
    placedWords = []

    #initialize matrix
    m = matrix.letterMatrix(size, size)

    #place first word
    x, y = solver.startingPosition(m, cleanWords[0])
    firstWord = [cleanWords.pop(0), x, y, True]
    m = matrix.addWord(firstWord[1],firstWord[2],firstWord[3],firstWord[0],m)
    placedWords.append(firstWord)

    #start recursing
    m = recursivePlaceWords(m, placedWords, cleanWords)


    #m = solver.placeWords(m, cleanWords)
    matrix.printMatrix(m)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a square crossword from the given words.')
    parser.add_argument('words', metavar='W', type=str, nargs='+',
                        help='a word to place on crossword')
    parser.add_argument('--size', dest='size',
                        type=int, default=10,
                        help='the target crossword size as a number (default: 10x10).')

    args = parser.parse_args()
    main(args.size, args.words)
