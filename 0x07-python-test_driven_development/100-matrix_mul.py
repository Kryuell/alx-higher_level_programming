#!/usr/bin/python3
""" 100-matrix_mul """


def matrix_mul(m_a, m_b):
    # Check if m_a is a list of lists
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    # Check if m_a is not empty
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")

    # Check if m_b is a list of lists
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_b is not empty
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    # Check if m_a and m_b contain only numbers
    def check_numbers(matrix):
        for row in matrix:
            if not all(isinstance(element, (int, float)) for element in row):
                return False
        return True

    if not check_numbers(m_a):
        raise TypeError("m_a should contain only integers or floats")

    if not check_numbers(m_b):
        raise TypeError("m_b should contain only integers or floats")

    # Check if each row of m_a has the same size
    if any(len(row) != len(m_a[0]) for row in m_a[1:]):
        raise TypeError("each row of m_a must be of the same size")

    # Check if each row of m_b has the same size
    if any(len(row) != len(m_b[0]) for row in m_b[1:]):
        raise TypeError("each row of m_b must be of the same size")

    # Check if number of columns in m_a is equal to number of rows in m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

# Example usage:
# print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
# print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
