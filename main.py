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
    cleanWords = sanitizeWords(args.words)
    m = matrix.letterMatrix(args.size, args.size)
    m = solver.stupidlyPlaceWords(m, cleanWords)
    matrix.printMatrix(m)
