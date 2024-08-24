import re

import pytest
from hypothesis import given
from hypothesis import strategies as st

from pynanoid import generate, non_secure_generate
from pynanoid.nanoid import (
    ALPHABET,
    generate_custom,
)
from pynanoid.nanoid import (
    generate as py_generate,
)
from pynanoid.nanoid import (
    non_secure_generate as py_non_secure_generate,
)


@given(
    alphabet=st.text(min_size=1),
    size=st.integers(min_value=1, max_value=5000),
)
@pytest.mark.parametrize(
    "generate_fn",
    [generate, py_generate],
    ids=["rust", "python"],
)
def test_correct_length(alphabet: str, size: int, generate_fn):  # noqa: ANN001
    assert len(generate_fn(alphabet, size)) == size


@given(
    alphabet=st.text(min_size=1),
    size=st.integers(min_value=1, max_value=5000),
)
@pytest.mark.parametrize(
    "generate_fn",
    [non_secure_generate, py_non_secure_generate],
    ids=["rust", "python"],
)
def test_correct_length_non_secure(alphabet: str, size: int, generate_fn):  # noqa: ANN001
    assert len(generate_fn(alphabet, size)) == size


@pytest.mark.parametrize(
    "generate_fn",
    [generate, py_generate],
    ids=["rust", "python"],
)
def test_has_no_collisions(generate_fn):  # noqa: ANN001
    count = 100_000
    used = set()
    for _ in range(count):
        id_ = generate_fn()
        assert id_ not in used
        used.add(id_)


@given(size=st.integers(min_value=1, max_value=5000))
@pytest.mark.parametrize(
    "generate_fn",
    [generate, py_generate],
    ids=["rust", "python"],
)
def test_generates_url_friendly_id(generate_fn, size: int):  # noqa: ANN001
    regex = re.compile(r"^[0-9A-Za-z_-]+$")
    id_ = generate_fn(size=size)
    assert len(id_) == size
    assert regex.match(id_)


@given(size=st.integers(min_value=1, max_value=5000))
@pytest.mark.parametrize(
    "generate_fn",
    [non_secure_generate, py_non_secure_generate],
    ids=["rust", "python"],
)
def test_generates_url_friendly_id_non_secure(generate_fn, size: int):  # noqa: ANN001
    regex = re.compile(r"^[0-9A-Za-z_-]+$")
    id_ = generate_fn(size=size)
    assert len(id_) == size
    assert regex.match(id_)


@given(size=st.integers(min_value=1, max_value=5000))
@pytest.mark.parametrize(
    "generate_fn",
    [generate, py_generate],
    ids=["rust", "python"],
)
def test_error_on_empty_alphabet(generate_fn, size: int):  # noqa: ANN001
    with pytest.raises(ValueError, match="alphabet cannot be empty"):
        generate_fn(alphabet="", size=size)


@given(size=st.integers(min_value=1, max_value=5000))
@pytest.mark.parametrize(
    "generate_fn",
    [non_secure_generate, py_non_secure_generate],
    ids=["rust", "python"],
)
def test_error_on_empty_alphabet_non_secure(generate_fn, size: int):  # noqa: ANN001
    with pytest.raises(ValueError, match="alphabet cannot be empty"):
        generate_fn(alphabet="", size=size)


@given(alphabet=st.text(min_size=1))
@pytest.mark.parametrize(
    "generate_fn",
    [generate, py_generate],
    ids=["rust", "python"],
)
def test_error_on_zero_size(generate_fn, alphabet: str):  # noqa: ANN001
    with pytest.raises(ValueError, match="size cannot be (less than 1|zero)"):
        generate_fn(alphabet, size=0)


@given(alphabet=st.text(min_size=1))
@pytest.mark.parametrize(
    "generate_fn",
    [non_secure_generate, py_non_secure_generate],
    ids=["rust", "python"],
)
def test_error_on_zero_size_non_secure(generate_fn, alphabet: str):  # noqa: ANN001
    with pytest.raises(ValueError, match="size cannot be (less than 1|zero)"):
        generate_fn(alphabet, size=0)


def test_generate_custom_randgen():
    sequence = [2, 255, 3, 7, 7, 7, 7, 7, 0, 1]

    def rand(size: int) -> bytes:
        random_bytes = []
        for i in range(0, size, len(sequence)):
            random_bytes += sequence[0 : size - i]
        return bytes(random_bytes)

    assert generate_custom(rand, "abcde", 4) == "cdac"


def test_default_alphabet_ascii():
    regex = re.compile(r"^[0-9A-Za-z_-]+$")
    assert regex.match(ALPHABET)
