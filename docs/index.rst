.. src documentation master file, created by
   sphinx-quickstart on Fri Aug 23 20:51:52 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyNanoID's documentation
===================================

.. toctree::
   :hidden:
   :caption: API documentation

   pynanoid/index

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff
   :alt: Ruff
.. image:: https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpdm-project%2F.github%2Fbadge.json
   :target: https://github.com/arunanshub/pynanoid
   :alt: PDM
.. image:: https://img.shields.io/pypi/pyversions/pynanoid
   :target: https://pypi.org/project/pynanoid
   :alt: PyPI - Python Version
.. image:: https://img.shields.io/pypi/v/pynanoid?color=green
   :alt: PyPI - Version
.. image:: https://img.shields.io/coverallsCoverage/github/arunanshub/pynanoid
   :alt: Coveralls code coverage

A tiny, secure, URL-friendly, unique string ID generator for Python, written in Rust.

- **Safe.** It uses hardware random generator. Can be used in clusters.
- **Fast.** 2-3 times faster than Python based generator.
- **Compact.** It uses a larger alphabet than UUID (``A-Za-z0-9_-``). So ID size
  was reduced from 36 to 21 symbols.

.. end no-heading

Installation
============

.. code-block:: shell-session

   $ pip install pynanoid

Usage
=====

.. code-block:: python

   from pynanoid import generate

   print(generate())

Symbols ``-,.()`` are not encoded in the URL. If used at the end of a link they
could be identified as a punctuation symbol.

The Rust based high-performance generator is used by default if available. You can
also use pure-Python based generator as shown :ref:`here <python-based-generator>`.

.. note::

   If Rust based implementation is not available, the pure-Python generator will
   be automatically used.

If you want to reduce ID length (and increase the probability of collisions),
you can pass the length as an argument.

.. code-block:: python

   from pynanoid import generate

   print(generate(size=10))

Don’t forget to check the safety of your ID length in ID `collision probability
calculator <https://zelark.github.io/nano-id-cc/>`_.


Custom Alphabet or Length
-------------------------

If you want to change the ID's alphabet or length, you can pass the alphabet as
the first argument and the size as the second argument.

.. code-block:: python

   from pynanoid import generate

   print(generate("1234567890abcdef", 10))

Non-secure generator is also available.

.. code-block:: python

   from pynanoid import non_secure_generate

   print(non_secure_generate())

.. warning::

   Non-secure generator uses :func:`random.random` internally. Hence it is not
   recommended for generating tokens or secrets.

.. _python-based-generator:

Force Use Pure-Python Generator
-------------------------------

If you want to use the pure-Python generator, you can use functions provided in
:mod:`pynanoid.nanoid`.

.. code-block:: python

   from pynanoid.nanoid import generate, non_secure_generate

   print(generate())
   print(non_secure_generate())


Benchmarks
==========

.. raw:: html
   :file: ../assets/benchmark.svg

We benchmark using `pytest-benchmark <https://pytest-benchmark.readthedocs.io/en/latest/>`_. You
can find the benchmark script in the `tests` directory.

You can run the benchmarks using the following command:

.. code-block:: shell-session

   $ pytest tests/benchmark.py --benchmark-histogram=assets/benchmark.svg


Credits
=======

- Andrey Sitnik for `Nano ID <https://github.com/ai/nanoid>`_.
- Paul Yuan (`@puyuan <https://github.com/puyuan>`_) for `py-nanoid
  <https://github.com/puyuan/py-nanoid>`_.
