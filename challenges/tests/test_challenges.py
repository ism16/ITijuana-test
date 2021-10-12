import pytest
import sys
import os
import mock
import builtins

sys.path.append(os.path.split(os.path.split(os.path.dirname(os.path.realpath( __file__ )))[0])[0])

from challenges.math import *

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