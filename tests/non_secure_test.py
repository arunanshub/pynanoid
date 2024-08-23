from sys import maxsize

from hypothesis import given
from hypothesis import strategies as st

from pynanoid import non_secure_generate
from pynanoid.constants import ALPHABET


@given(st.integers(min_value=1, max_value=5000))
def test_changes_id_length(size: int):
    assert len(non_secure_generate(size=size)) == size


def test_generates_url_friendly_id():
    for _ in range(10):
        id_ = non_secure_generate()
        assert len(id_) == 21
        for j in range(len(id_)):
            assert ALPHABET.find(id_[j]) != -1


def test_has_flat_distribution():
    count = 100 * 1000
    length = len(non_secure_generate())

    chars = {}
    for _ in range(count):
        id_ = non_secure_generate()
        for j in range(len(id_)):
            char = id_[j]
            if not chars.get(char):
                chars[char] = 0
            chars[char] += 1

    assert len(chars.keys()) == len(ALPHABET)

    max_ = 0
    min_ = maxsize
    for k in chars:
        distribution = (chars[k] * len(ALPHABET)) / float(count * length)
        max_ = max(distribution, max_)
        min_ = min(distribution, min_)
    assert max_ - min_ <= 0.05


def test_has_no_collisions():
    count = 100 * 1000
    used = {}
    for _ in range(count):
        id_ = non_secure_generate()
        assert id_ not in used
        used[id_] = True
