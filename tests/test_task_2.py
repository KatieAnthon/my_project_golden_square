import pytest
from lib.task_2 import *

def test_grammar_checker_shows_True_when_correct():
    result = grammar_checker("Hello, how are you Simon?")
    assert result == True

def test_grammar_checker_shows_False_when_incorrect():
    result = grammar_checker("no i haven't corrected my grammar")
    assert result == False

def test_grammar_shows_false_for_1_part_wrong():
    result = grammar_checker("First letter is capital but this doesn't end correctly")
    assert result == "Check the ending punctuation."

def test_grammar_shows_false_when_First_wrong():
    result = grammar_checker("no, there are no capital's here!")
    assert result == "Your starting capital letter is missing."

def test_grammar_works_with_full_stop():
    result = grammar_checker("Finally, it is correct.")
    assert result == True
