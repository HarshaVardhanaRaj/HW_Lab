import numpy as np

# 0D Array (Scalar)
arr_0d = np.array(7)
print("0D Array = ",arr_0d)
print("Shape = ",arr_0d.shape)
print("Dimensions = ",arr_0d.ndim)
print()


# 1D Array (Vector)
arr_1d = np.array([1,2,3,4])
print("1D Array = ",arr_1d)
print("Shape = ",arr_1d.shape)
print("Dimensions = ",arr_1d.ndim)
print()


# 2D Array (Matrix)
arr_2d = np.array([[1,2,3],[4,5,6]])
print("2D Array = ",arr_2d)
print("Shape = ",arr_2d.shape)
print("Dimensions = ",arr_2d.ndim)
print()


# 3D Array (Tensor)
arr_3d = np.array([ [ [1,2],[3,4] ] , [ [5,6],[7,8] ] ])
print("3D Array = ",arr_3d)
print("Shape = ",arr_3d.shape)
print("Dimensions = ",arr_3d.ndim)
print()
