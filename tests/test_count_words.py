from lib.count_words import *

def test_count_words_in_string_delimeter_is_spaces():
    result = count_words("Hello my name is Jeffrey")
    assert result == 5

def test_count_words_in_string_delimeter_is_comma():
    result = count_words("hiya,how,many,words,are,here")
    assert result == 6

def test_count_words_in_string_delimeter_is_hyphen():
    result = count_words("hiya-what's-your-name?")
    assert result == 4

def test_count_words_in_string_delimeter_is_mixed():
    result = count_words("hiya-when,did-you get here: Peter?")
    assert result == 7