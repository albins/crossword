#!/usr/bin/env python2
import argparse


def usage():
    return ""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a square crossword from the given words.')
    parser.add_argument('words', metavar='W', type=str, nargs='+',
                        help='a word to place on crossword')
    parser.add_argument('--size', dest='size',
                        type=int, default=10,
                        help='the target crossword size as a number (default: 10x10).')
    args = parser.parse_args()
    print "Generate crossword of " + str(args.size) + "x" + str(args.size) + " using " + str(args.words) + "."
