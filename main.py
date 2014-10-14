#!/usr/bin/env python2
import argparse
import lettermatrix as matrix

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a square crossword from the given words.')
    parser.add_argument('words', metavar='W', type=str, nargs='+',
                        help='a word to place on crossword')
    parser.add_argument('--size', dest='size',
                        type=int, default=10,
                        help='the target crossword size as a number (default: 10x10).')

    args = parser.parse_args()
    m = matrix.letterMatrix(args.size, args.size)
    m = matrix.addWord(1, 1 , True, args.words[0], m)
    matrix.printMatrix(m)
