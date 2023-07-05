#!/usr/bin/python3

"""Function module that multiplies two matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Prints and returns multiplication of two matrices.
    Arg:
    m_a (list of lists of ints/floats): First matrix argument.
    m_b (list of lists of ints/floats): Second matrix argument.
    """

    return (np.matmul(m_a, m_b))
