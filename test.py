from lettermatrix import letterMatrix, addWord, printMatrix, EMPTY_CELL
from nose.tools import assert_equal, assert_not_equal, assert_raises, raises

class TestBasicMatrixOperations(object):
    def setUp(self):
        # always make sure self.matrix is a fresh 10x10 matrix
        self.matrix = letterMatrix(10,10)

    def test_new_matrix(self):
        m = letterMatrix(4,4)
        for row in m:
            for cell in row:
                assert cell == EMPTY_CELL

    def test_add_horizontal(self):
        word = "pig"
        nm = addWord(3,4, True, word, self.matrix)
        printMatrix(self.matrix)
        correct_column = nm[3]
        correct_word = correct_row[3:]
        print correct_word
        print correct_row
        assert False

    def test_add_vertical(self):
        assert False

    def test_add_overlapping(self):
        assert False

    def test_add_impossible(self):
        assert False

    def test_new_word_fail(self):
        assert False

    def test_new_word_succeed(self):
        assert False

# nm = addWord(3,4,False,'hej',m)
# if nm != False:
#     m = nm

# nm = addWord(6,3,False,'boll',m)
# if nm:
#     m = nm

# nm = addWord(3,4,True,'hoho',m)
# if nm != False:
#     m = nm

# nm = addWord(6,0,True,'cake',m)
# if nm != False:
#     m = nm

if __name__ == '__main__':
    printMatrix(m)
