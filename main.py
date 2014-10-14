#!/usr/bin/env python2
import argparse
import lettermatrix as matrix
import findnext as solver

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a square crossword from the given words.')
    parser.add_argument('words', metavar='W', type=str, nargs='+',
                        help='a word to place on crossword')
    parser.add_argument('--size', dest='size',
                        type=int, default=10,
                        help='the target crossword size as a number (default: 10x10).')

    args = parser.parse_args()
    
    #initialize new words and list of placed words
    cleanWords = sanitizeWords(args.words)
    placedWords = []
    
    #initialize matrix
    m = matrix.letterMatrix(args.size, args.size)
    
    #add first word from list
    firstWord = solver.stupidlyPlaceWords(m, cleanWords)
    m = matrix.addWord(firstWord[1],firstWord[2],firstWord[3],firstWord[0],m)
    placedWords.append(firstWord)
    cleanWords.pop(0)
    nextWord = solver.placeNextWord(m, placedWords, cleanWords)
    m = matrix.addWord(nextWord[1],nextWord[2],nextWord[3],nextWord[0],m)
    placedWords.append(nextWord)
    cleanWords.pop(0)
    matrix.printMatrix(m)
    print placedWords
    nextNextWord = solver.placeNextWord(m, placedWords, cleanWords)
    m = matrix.addWord(nextNextWord[1],nextNextWord[2],nextNextWord[3],nextNextWord[0],m)
    matrix.printMatrix(m)



