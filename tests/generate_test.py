from sys import maxsize

from hypothesis import given
from hypothesis import strategies as st

from nanoid import generate


def test_has_flat_distribution():
    count = 100 * 1000
    length = 5
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    chars = {}
    for _ in range(count):
        id_ = generate(alphabet, length)
        for j in range(len(id_)):
            char = id_[j]
            if not chars.get(char):
                chars[char] = 0
            chars[char] += 1

    assert len(chars.keys()) == len(alphabet)

    max_ = 0
    min_ = maxsize
    for k in chars:
        distribution = (chars[k] * len(alphabet)) / float(count * length)
        min_ = min(distribution, min_)
        max_ = max(distribution, max_)
    assert max_ - min_ <= 0.05


def test_has_no_collisions():
    count = 100 * 1000
    used = {}
    for _ in range(count):
        id_ = generate()
        assert id_ not in used
        used[id_] = True


def test_has_options():
    count = 100 * 1000
    for _ in range(count):
        assert generate("a", 5) == "aaaaa"
        assert len(generate(alphabet="12345a", size=3)) == 3


@given(st.text(min_size=1), st.integers(min_value=1, max_value=5000))
def test_same_size(alphabet: str, size: int):
    assert len(generate(alphabet, size)) == size