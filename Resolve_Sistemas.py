import numpy as np

A = np.array([[2, 3], [1, -5]])
B = np.array([4, 2])

x = np.dot(np.linalg.inv(A), B)

print(A)
print(B)



print("S(a, b) = ", x.ravel())