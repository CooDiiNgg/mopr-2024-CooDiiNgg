import pytest
import os

def run_tests():
    path = os.path.dirname(os.path.abspath(__file__))
    tests_1 = os.path.join(path, "test_homework_vectors_problem1.py")
    tests_2 = os.path.join(path, "test_homework_vectors_problem2.py")
    pytest.main([tests_1, tests_2])
    print("All tests passed!")