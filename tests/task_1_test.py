import pytest
from lib.task_1 import *

def test_that_200_words_is_1_min():
    string = "one "
    string_length_200 = string*200
    result = reading_time(string_length_200)
    assert result == "Reading time = 1 Minutes"

def test_that_more_than_12000_is_1_hour():
    string = "two "
    string_length_12000 = string * 12000
    result = reading_time(string_length_12000)
    assert result == "Reading time = 1 Hours"

def test_that_commas_and_dashes_are_considered_delim():
    string = " two,my-name"
    string_length_600 = string*200
    result = reading_time(string_length_600)
    assert result == "Reading time = 3 Minutes"

def test_raises_error_for_empty_string():

    with pytest.raises(Exception) as e:
        reading_time("")
    message = str(e.value)
    print(f"Exception message: {str(e.value)}")
    assert message == "Can't estimate time for empty text!"

def test_a_decimal_minute_value():
    string = "one "
    string_length_355 = string*355
    result = reading_time(string_length_355)
    assert result == "Reading time = 1 Minutes"

