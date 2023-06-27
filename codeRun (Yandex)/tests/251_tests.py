import sys
sys.path.append("..")

import pytest
import two

@pytest.mark.parametrize(
    ("s1", "s2", "result"),
    (
        ("aabbcdd", "abc", 4),
        ("abc", "abc", 3),
        ("kncjdsaf", "kncjdsaf", 8),
        ("cdbcdbdccb", "dcb", 3),
        ("abc", "d", 0),
        ("abdcaaaaab", "abc", 7),
        ("a", "a", 1),
        ("ab", "b", 1),
        ("lkasdjfoijbbbbbboiasdjfijb", "b", 1),
        ("lkasdjfoijbbbbbboiasdjfijbb", "b", 1),
        ("abbbbbbcdabbbbcdabcdabbbc", "abc", 3),
        ("aabbbcaaab", "abc", 3),
        ("a", "abc", 0),
        ("abd", "abc", 0)

    )
)
def test_solution(s1, s2, result):
    assert two.solution(s1, s2) == result
    

