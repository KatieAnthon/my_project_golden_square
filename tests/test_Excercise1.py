from lib.Excercise1 import *

def test_say_hello_returns_lc_name():
    result = say_hello("kay")
    assert result == "hello kay"

