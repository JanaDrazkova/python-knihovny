# test_40_most_frequent.py

import pytest
from tasks.task_40_most_frequent import most_frequent

def test_most_frequent():
    assert most_frequent([1,1,2,2,2,3]) == 2
    assert most_frequent(["a","b","a","a","c"]) == "a"
    assert most_frequent([True, False, True, True]) == True
    assert most_frequent([42]) == 42
    assert most_frequent(["x", "y", "x", "z", "x"]) == "x"
    assert most_frequent([3,3,3,2,2,1]) == 3

