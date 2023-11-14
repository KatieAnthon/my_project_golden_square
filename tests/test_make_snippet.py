from lib.make_snippet import *

def test_make_snippet_longer_than_5():
    result = make_snippet("Hello, how are you doing? My name is Katie")
    assert result == "Hello, how are you doing?..."

# if there is an empty string

def test_empty_string():
    result = make_snippet("")
    assert result == ""

def test_string_shorter_than_5_words():
    result = make_snippet("Hiya, I'm good")
    assert result == "Hiya, I'm good"

def test_string_5_words():
    result = make_snippet("First Second Third Fourth Fifth")
    assert result == "First Second Third Fourth Fifth"