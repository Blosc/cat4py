import cat4py as cat
import pytest
import numpy as np


@pytest.mark.parametrize("shape, pshape1, pshape2, itemsize",
                         [
                             ([2], [2], [2], 8),
                             ([20, 134, 13], [3, 13, 5], [3, 2, 4], 4),
                             ([12, 13, 14, 15, 16], None, [3, 3, 5, 3, 3], 8)
                         ])
def test_copy(shape, pshape1, pshape2, itemsize):

    a = cat.Container(pshape=pshape1, itemsize=itemsize)

    size = int(np.prod(shape))

    buffer = bytes(size * itemsize)

    a.from_buffer(shape, buffer)

    b = a.copy(pshape=pshape2)

    buffer2 = b.to_buffer()

    assert buffer == buffer2
