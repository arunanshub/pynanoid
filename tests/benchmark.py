import pytest
from pytest_benchmark.fixture import (  # type: ignore[import-untyped]
    BenchmarkFixture,
)

from pynanoid import generate as rust_generate
from pynanoid.constants import ALPHABET, SIZE
from pynanoid.nanoid import generate as python_generate


@pytest.mark.parametrize("size", [SIZE])
def test_rust_method(benchmark: BenchmarkFixture, size: int):
    benchmark(rust_generate, ALPHABET, size)


@pytest.mark.parametrize("size", [SIZE])
def test_python_method(benchmark: BenchmarkFixture, size: int):
    benchmark(python_generate, ALPHABET, size)
