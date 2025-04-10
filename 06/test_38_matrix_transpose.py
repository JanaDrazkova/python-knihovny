# test_38_matrix_transpose.py

import pytest
from tasks.task_38_matrix_transpose import matrix_transpose

def test_matrix_transpose():
    assert matrix_transpose([[1,2],[3,4]]) == [[1,3],[2,4]]
    assert matrix_transpose([[1,2,3]]) == [[1],[2],[3]]
    assert matrix_transpose([[1],[2],[3]]) == [[1,2,3]]
    assert matrix_transpose([]) == []
    assert matrix_transpose([[5]]) == [[5]]
    assert matrix_transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]

