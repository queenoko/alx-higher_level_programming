#!/usr/bin/python3
"""
Function module that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """Function that multiplies two matrices

    Arg:
    m_a (list of lists of int/float): Matrix to multiply
    m_b (list of lists of int/float): Matrix to multiply

    Raises:
    TypeError: If m_a or m_b is not a list
    TypeError: If m_a or m_b is not a list of lists
    TypeError: If one element of the list of lists is not int/float
    TypeError: If row of m_a or m_b are not the same size
    ValueError: If m_a or m_b is empty
    ValueError: If m_a and m_b cannot be multiplied

    Returns:
    New list which is the outcome of the multiplication
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row1, list) for row1 in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row1, list) for row1 in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(element1, int) or isinstance(element1, float))
               for element1 in [number for row1 in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element1, int) or isinstance(element1, float))
               for element1 in [number for row1 in m_b for number in row1]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row1) == len(m_a[0]) for row1 in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row1) == len(m_b[0]) for row1 in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_num = []
    for y in range(len(m_b[0])):
        row_matrix = []
        for z in range(len(m_b)):
            row_matrix.append(m_b[j][i])
        matrix_num.append(row_matrix)

    matrix_num2 = []
    for row1 in m_a:
        row_matrix = []
        for column1 in matrix_num:
            product_num = 0
            for q in range(len(matrix_num[0])):
                product_num += row1[q] * column1[q]
            row_matrix.append(product_num)
        matrix_num2.append(row_matrix)

    return matrix_num2
