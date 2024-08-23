from sys import maxsize

from pynanoid import generate, non_secure_generate
from pynanoid.constants import ALPHABET


def test_flat_distribution():
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
        max_ = max(distribution, max_)
        min_ = min(distribution, min_)
    assert max_ - min_ <= 0.05


def test_generates_url_friendly_id():
    for _ in range(10):
        id_ = generate()
        assert len(id_) == 21
        for j in range(len(id_)):
            assert id_[j] in ALPHABET


def test_has_no_collisions():
    count = 100 * 1000
    used = {}
    for _ in range(count):
        id_ = generate()
        assert id_ not in used
        used[id_] = True


def test_has_options():
    assert generate("a", 5) == "aaaaa"


def test_non_secure_ids():
    for _ in range(10000):
        nanoid = non_secure_generate()
        assert len(nanoid) == 21


def test_non_secure_short_ids():
    for _ in range(10000):
        nanoid = non_secure_generate("12345a", 3)
        assert len(nanoid) == 3


def test_short_secure_ids():
    for _ in range(10000):
        nanoid = generate("12345a", 3)
        assert len(nanoid) == 3
