#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices
"""

def matrix_mul(m_a, m_b):
    """This function multiplies two matrices

    Args:
        m_a (list of lists of int/float): Matrix to be multiplied
        m_b (list of lists of int/float): Matrix to be multiplied

    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        TypeError: If rows of m_a or m_b are not the same size
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied

    Returns:
        A new list which is the outcome of the multiplication
    """

    # Check if inputs are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if inputs are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if matrices are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check if all elements are integers or floats
    if not all(isinstance(element, (int, float)) for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, (int, float)) for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    # Check if all rows have the same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if the number of columns in m_a is equal to the number of rows in m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for row_a in m_a:
        new_row = []
        for col_b in range(len(m_b[0])):
            product = 0
            for i in range(len(row_a)):
                product += row_a[i] * m_b[i][col_b]
            new_row.append(product)
        result.append(new_row)

    return result
