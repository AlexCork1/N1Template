import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'odgovori.json'))
assert os.path.exists(file_path), "Manjka datoteka odgovori.json"

from code import square, is_even

# testiranje funkcij
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-1) == 1

def test_is_even():
    assert is_even(0) is True
    assert is_even(3) is False
    assert is_even(4) is True

# testi teorija
def test_q1():
    with open(file_path, encoding='utf-8') as f:
        answers = json.load(f)
    assert answers["q1"] == "A) A prime number"

def test_q2():
    with open(file_path, encoding='utf-8') as f:
        answers = json.load(f)
    assert answers["q2"] == "D) 0"