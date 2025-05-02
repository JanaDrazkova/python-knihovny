# test_36_sum_nested_list.py

import pytest
from tasks.task_36_sum_nested_list import sum_nested_list

def test_sum_nested_list():
    assert sum_nested_list([1, 2, [3, 4], 5]) == 15
    assert sum_nested_list([]) == 0
    assert sum_nested_list([[[1]], 2, [3, [4]]]) == 10
    assert sum_nested_list([0, [0, [0]]]) == 0
    assert sum_nested_list([10, [20, [30, [40]]]]) == 100
    assert sum_nested_list([1, [2], 3, [4, [5, [6]]]]) == 21

