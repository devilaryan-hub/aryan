import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[6, 5, 4], [3, 2, 1]])

addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

print("Element-wise Addition:\n", addition)
print("Element-wise Subtraction:\n", subtraction)
print("Element-wise Multiplication:\n", multiplication)
print("Element-wise Division:\n", division)

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

dot_product = np.dot(vector1, vector2)
print("Dot Product:", dot_product)

cross_product = np.cross(vector1, vector2)
print("Cross Product:\n", cross_product)
