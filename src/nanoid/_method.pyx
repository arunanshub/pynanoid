# distutils: language=c++
cimport cython

from os import urandom
from libc.math cimport log, ceil
from libcpp.vector cimport vector


cdef const unsigned char[:] algorithm_generate(int size):
    """Generate random bytes of given size."""
    return urandom(size)


@cython.wraparound(False)
@cython.boundscheck(False)
cpdef str method(str alphabet, size_t size):
    cdef:
        const unsigned char[:] alphabet_encoded = alphabet.encode('utf-8')
        unsigned int alphabet_len = len(alphabet_encoded)
        unsigned int mask = 1

    if alphabet_len > 1:
        mask = (2 << <int>(log(alphabet_len - 1) / log(2))) - 1
    cdef int step = <int>ceil(1.6 * mask * size / alphabet_len)

    cdef:
        const unsigned char[:] random_bytes
        size_t i
        unsigned int random_byte
        vector[unsigned char] result
        bint is_done = False

    result.reserve(size)

    while True:
        random_bytes = algorithm_generate(step)

        with nogil:
            for i in range(<size_t>step):
                random_byte = random_bytes[i] & mask
                if random_byte >= alphabet_len:
                    continue
                if not alphabet_encoded[random_byte]:
                    continue
                result.push_back(alphabet_encoded[random_byte])

                if result.size() == size:
                    is_done = True
                    break

        if is_done:
            return result.const_data()[:size].decode("utf-8")
