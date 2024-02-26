import numpy as np
from scipy.linalg import solve

def solve_matrix_problem_1():
    """
    Solves the first matrix problem:
    3x1 + x2 - x3 = 2
    x1 + 4x2 + x3 = 12
    2x1 + x2 + 2x3 = 10
    """
    # Define the coefficient matrix (left side of the equations)
    A = np.array([[3, 1, -1],
                  [1, 4, 1],
                  [2, 1, 2]])

    # Define the constant vector (right side of the equations)
    b = np.array([2, 12, 10])

    # Solve the system of equations
    x = solve(A, b)

    return x

def solve_matrix_problem_2():
    """
    Solves the second matrix problem:
    x1 - 10x2 + 2x3 + 4x4 = 2
    3x1 + x2 + 4x3 + 12x4 = 12
    9x1 + 2x2 + 3x3 + 4x4 = 21
    -x1 + 2x2 + 7x3 + 3x4 = 37
    """
    # Define the coefficient matrix (left side of the equations)
    A = np.array([[1, -10, 2, 4],
                  [3, 1, 4, 12],
                  [9, 2, 3, 4],
                  [-1, 2, 7, 3]])

    # Define the constant vector (right side of the equations)
    b = np.array([2, 12, 21, 37])

    # Solve the system of equations
    x = solve(A, b)

    return x

# Run and print results for the first matrix problem
print("Solution for the first matrix problem:")
print(solve_matrix_problem_1())

# Run and print results for the second matrix problem
print("\nSolution for the second matrix problem:")
print(solve_matrix_problem_2())
