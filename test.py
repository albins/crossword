from lettermatrix import letterMatrix, addWord, printMatrix, EMPTY_CELL, row, column, filter_empty
from nose.tools import assert_equal, assert_not_equal, assert_raises, raises
import nose

class TestBasicMatrixOperations(object):

    def setUp(self):
        # always make sure self.matrix is a fresh 10x10 matrix
        self.matrix = letterMatrix(10, 10)

    def test_new_matrix(self):
        m = letterMatrix(4,4)
        for row in m:
            for cell in row:
                assert cell == EMPTY_CELL

    def test_add_horizontal(self):
        word = "pig"
        nm = addWord(3,4, True, word, self.matrix)
        letters_row = filter_empty(row(nm, 4))
        printMatrix(self.matrix)
        assert ''.join(letters_row) == word

    def test_add_vertical(self):
        word = "pig"
        nm = addWord(3,4, False, word, self.matrix)
        letters_column = filter_empty(column(nm, 3))
        printMatrix(self.matrix)
        assert ''.join(letters_column) == word

    def test_add_overlapping_possible(self):
        nm = addWord(6,3,False,'boll',self.matrix)
        nm = addWord(3,4,True,'hoho',nm)
        # We succeeded:
        assert nm
        letters_column = filter_empty(column(nm, 6))
        print letters_column
        printMatrix(self.matrix)
        # ...and the first word is still there:
        assert ''.join(letters_column) == 'boll'

    def test_add_impossible(self):
        nm = addWord(6,3,False,'byll',self.matrix)
        nm = addWord(3,4,True,'hoho',nm)
        assert not nm

    def test_add_all_spaces_single_letter_even(self):
        letter = "a"
        test_matrix = self.matrix
        # fill the matrix one space at a time, only even column
        # numbers
        for x in range(0,10,2):
            for y in range(0,10):
                print  str(x) + ", " + str(y)
                assert test_matrix
                printMatrix(test_matrix)
                test_matrix = addWord(x, y, False, letter, test_matrix)
        # and assert that the matrix is actually filled:
        for column_no in range(0,10,2):
            for cell in column(test_matrix, column_no):
                assert cell == letter

    def test_add_all_spaces_single_letter_odd(self):
        letter = "a"
        test_matrix = self.matrix
        # fill the matrix one space at a time, only odd column
        # numbers
        for x in range(1,10,2):
            for y in range(0,10):
                print  str(x) + ", " + str(y)
                assert test_matrix
                printMatrix(test_matrix)
                test_matrix = addWord(x, y, False, letter, test_matrix)
        # and assert that the matrix is actually filled:
        for column_no in range(1,10,2):
            for cell in column(test_matrix, column_no):
                assert cell == letter

    def test_add_fringe_word(self):
        word = 'boll'
        nm = addWord(9,0,False,word, self.matrix)
        printMatrix(nm)
        assert nm
        letters_column = ''.join(filter_empty(column(nm,9)))
        assert letters_column == word
if __name__ == '__main__':
    nose.main()
