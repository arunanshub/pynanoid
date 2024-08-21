from nanoid.resources import ALPHABET


def test_has_no_duplicates():
    for i in range(len(ALPHABET)):
        assert ALPHABET.rindex(ALPHABET[i]) == i


def test_is_string():
    assert isinstance(ALPHABET, str)
