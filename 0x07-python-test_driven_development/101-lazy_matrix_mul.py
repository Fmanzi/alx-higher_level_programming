#!/usr/bin/python3
"""
Lazy matrix multiplication using NumPy
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        np.ndarray: The product of m_a and m_b.

    Raises:
        ValueError: If m_a and m_b cannot be multiplied.

    """
    try:
        np_m_a = np.array(m_a)
        np_m_b = np.array(m_b)
        result = np.dot(np_m_a, np_m_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
