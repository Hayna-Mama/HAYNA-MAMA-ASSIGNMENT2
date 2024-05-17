import numpy as np

#Example 1

#2x2 Matrix
a = np.array([[1,2,3], [3,4,5]])
b = np.array([[6,7,8], [9,10,11]])

# Dot Method
result_dot = np.dot(a, b)
print("Dot Product of a and b:")
print(result_dot)

# Transpose Method
result_transpose = a.transpose()
print("\nTranspose of a:")
print(result_transpose)

# linalg.inv Method
result_inv = np.linalg.inv(a)
print("\nInverse of a:")
print(result_inv)

# linalg.det Method
result_det = np.linalg.det(a)
print("\nDeterminant of a:")
print(result_det)

# flatten method
result_flatten = a.flatten()
print("\nFlattened a:")
print(result_flatten)


#Example 2

#2x2 Matrix
c = np.array([[12,13,14], [15,16,17]])
d = np.array([[18,19,20], [21,22,23]])

# Dot Method
result_dot = np.dot(c, d)
print("Dot Product of c and d:")
print(result_dot)

# Transpose Method
result_transpose = c.transpose()
print("\nTranspose of c:")
print(result_transpose)

# linalg.inv Method
result_inv = np.linalg.inv(c)
print("\nInverse of c:")
print(result_inv)

# linalg.det Method
result_det = np.linalg.det(c)
print("\nDeterminant of c:")
print(result_det)

# flatten method
result_flatten = c.flatten()
print("\nFlattened c:")
print(result_flatten)


#Example 

#2x2 Matrix
e = np.array([[24,25,26], [27,28,29]])
f = np.array([[30,31,32], [33,34,35]])

# Dot Method
result_dot = np.dot(e, f)
print("Dot Product of e and f:")
print(result_dot)

# Transpose Method
result_transpose = e.transpose()
print("\nTranspose of e:")
print(result_transpose)

# linalg.inv Method
result_inv = np.linalg.inv(e)
print("\nInverse of e:")
print(result_inv)

# linalg.det Method
result_det = np.linalg.det(e)
print("\nDeterminant of e:")
print(result_det)

# flatten method
result_flatten = e.flatten()
print("\nFlattened e:")
print(result_flatten)