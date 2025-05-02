# test_39_reverse_vowels.py

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

