import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from fibonacci import fibonacci


def test_seven_terms():
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_one_term():
    assert fibonacci(1) == [0]


def test_zero_terms():
    assert fibonacci(0) == []


if __name__ == "__main__":
    test_seven_terms()
    test_one_term()
    test_zero_terms()
    print("All tests passed")
