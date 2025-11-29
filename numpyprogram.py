import numpy as np

# Creating a 1D array
one_d = np.array([10, 20, 30, 40])

# Creating a 2D array
two_d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print("1D Array:", one_d)
print("Shape:", one_d.shape)
print("Dimensions:", one_d.ndim)
print("Data Type:", one_d.dtype)

print("\n2D Array:\n", two_d)
print("Shape:", two_d.shape)
print("Dimensions:", two_d.ndim)
print("Data Type:", two_d.dtype)
