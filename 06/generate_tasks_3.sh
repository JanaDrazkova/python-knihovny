#!/bin/bash

mkdir -p tasks

function write_task_and_test() {
  num=$1
  name=$2
  task_code=$3
  test_code=$4

  task_file="tasks/task_${num}_${name}.py"
  test_file="test_${num}_${name}.py"

  echo "# task_${num}_${name}.py" > "$task_file"
  echo -e "$task_code" >> "$task_file"

  echo "# test_${num}_${name}.py" > "$test_file"
  echo -e "$test_code" >> "$test_file"
}

write_task_and_test "36" "sum_nested_list" '
def sum_nested_list(nested: list) -> int:
    """
    Sečte všechna čísla v (potenciálně zanořeném) seznamu.
    Nápověda: isinstance(), rekurze
    """
' '
import pytest
from tasks.task_36_sum_nested_list import sum_nested_list

def test_sum_nested_list():
    assert sum_nested_list([1, 2, [3, 4], 5]) == 15
    assert sum_nested_list([]) == 0
    assert sum_nested_list([[[1]], 2, [3, [4]]]) == 10
    assert sum_nested_list([0, [0, [0]]]) == 0
    assert sum_nested_list([10, [20, [30, [40]]]]) == 100
    assert sum_nested_list([1, [2], 3, [4, [5, [6]]]]) == 21
'


write_task_and_test "37" "longest_unique_substring" '
def longest_unique_substring(s: str) -> int:
    """
    Vrátí délku nejdelší podposloupnosti bez opakujících se znaků.
    """
' '
import pytest
from tasks.task_37_longest_unique_substring import longest_unique_substring

def test_longest_unique_substring():
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("pwwkew") == 3
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("abcdef") == 6
    assert longest_unique_substring("abccba") == 3
    assert longest_unique_substring("abba") == 2
    assert longest_unique_substring("tmmzuxt") == 5
'

write_task_and_test "38" "matrix_transpose" '
def matrix_transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Vrátí transponovanou matici.
    """
' '
import pytest
from tasks.task_38_matrix_transpose import matrix_transpose

def test_matrix_transpose():
    assert matrix_transpose([[1,2],[3,4]]) == [[1,3],[2,4]]
    assert matrix_transpose([[1,2,3]]) == [[1],[2],[3]]
    assert matrix_transpose([[1],[2],[3]]) == [[1,2,3]]
    assert matrix_transpose([]) == []
    assert matrix_transpose([[5]]) == [[5]]
    assert matrix_transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]
'

write_task_and_test "39" "reverse_vowels" '
def reverse_vowels(s: str) -> str:
    """
    Vrátí řetězec s přeházenými samohláskami v opačném pořadí.
    Ostatní znaky zůstávají na místě.
    """
' '
import pytest
from tasks.task_39_reverse_vowels import reverse_vowels

def test_reverse_vowels():
    assert reverse_vowels("hello") == "holle"
    assert reverse_vowels("leetcode") == "leotcede"
    assert reverse_vowels("aA") == "Aa"
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("") == ""
    assert reverse_vowels("bcdfg") == "bcdfg"
    assert reverse_vowels("AEIOU") == "UOIEA"
    assert reverse_vowels("racecar") == "racecar"
'

write_task_and_test "40" "most_frequent" '
def most_frequent(items: list) -> any:
    """
    Vrátí nejčastěji se vyskytující prvek v seznamu.
    """
' '
import pytest
from tasks.task_40_most_frequent import most_frequent

def test_most_frequent():
    assert most_frequent([1,1,2,2,2,3]) == 2
    assert most_frequent(["a","b","a","a","c"]) == "a"
    assert most_frequent([True, False, True, True]) == True
    assert most_frequent([42]) == 42
    assert most_frequent(["x", "y", "x", "z", "x"]) == "x"
    assert most_frequent([3,3,3,2,2,1]) == 3
'
