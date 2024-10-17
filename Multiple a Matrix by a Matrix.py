import numpy as np

matrix_1 = np.array([[1, 2, 3],
                   [4, 5, 7],
                  [8, 9, 10]])
matrix_2 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

result = np.dot(matrix_1, matrix_2)

print(f"The b vector is: \n {result}")
