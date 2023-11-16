# when you run this file, these next lines will show you the expected
# and actual outputs of the functions above.

from lib.exercise2 import *

def test_encode_works():
    result = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
    assert result == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"


def test_decode_works():
    result = decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
    assert result == "theswiftfoxjumpedoverthelazydog"