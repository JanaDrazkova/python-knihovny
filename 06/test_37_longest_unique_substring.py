# test_37_longest_unique_substring.py

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

