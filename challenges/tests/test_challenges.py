import pytest
import sys
import os
import mock
import builtins

sys.path.append(os.path.split(os.path.split(os.path.dirname(os.path.realpath( __file__ )))[0])[0])

from challenges.math import *
from challenges.questions import *
from challenges.games import *
from challenges.files import *

def test_question_1():
    assert [5, 10, 15, 20, 25, 30] == question_1(0, 40)
    assert [5, 10, 15, 20, 25, 30, 40] == question_1(0, 41)
    assert [5, 10, 15, 20, 25, 30, 40, 45, 50, 55, 60, 65] == question_1(0, 71)

def test_question_2():
    with mock.patch.object(builtins, 'input', lambda _: 4):
        assert question_2() == '10'
    with mock.patch.object(builtins, 'input', lambda _: 9):
        assert question_2() == '10'
    return

def test_question_3():
    assert '101' == question_3(5, 2)
    assert '12' == question_3(5, 3)
    assert '102' == question_3(11, 3)
    assert '133302' == question_3(2034, 4)

def test_perfect_square_generator():
    assert [x for x in perfect_square_generator(30)] == [1, 4, 9, 16, 25]
    assert [x for x in perfect_square_generator(10)] == [1, 4, 9]
    assert [x for x in perfect_square_generator(0)] == []
    assert [x for x in perfect_square_generator(1)] == []
    assert [x for x in perfect_square_generator(2)] == [1]

def test_Rook_class():
    rook = Rook('up 1, left 3, down 2')
    assert rook.distance == 6
    assert rook.steps == 4
    assert rook.euclidean == ((rook.x**2) + (rook.y**2))**(1/2)

def test_search_for_text():
    # text taken from: https://www.cltexam.com/example-test
    text = '''But I particularly remember one wild, snowy afternoon, soon after my 
        return in January: the children had all come up from dinner, loudly 
        declaring that they meant "to be naughty," and they had well kept their 
        resolution, though I had talked myself hoarse, and wearied every muscle 
        in my throat, in the vain attempt to reason them out of it. I had got 
        Tom pinned up in a corner, whence, I told him, he should not escape till 
        he had done his appointed task. Meantime, Fanny had possessed herself of 
        my work-bag, and was rifling its contents—and spitting into it besides. 
        I told her to let it alone, but to no purpose, of course.'''

    assert search_for_text('he should not escape till', text) == True
    assert search_for_text('let it alone', text) == True
    assert search_for_text('', text) == True
    assert search_for_text('dsafasdfasg', text) == False
    assert search_for_text('123412', text) == False
    assert search_for_text('But med', text) == False

def test_sum_columns_from_csv():
    assert sum_columns_from_csv('challenges/tests/testfile.csv', 0) == 15
    assert sum_columns_from_csv('challenges/tests/testfile.csv', 1) == 18
    assert sum_columns_from_csv('challenges/tests/testfile.csv', 2) == 21
    assert sum_columns_from_csv('challenges/tests/testfile.csv', 3) == 24