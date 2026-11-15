import numpy as np


# 1D array - a simple list, 'int8' keeps each number small (1 byte)
a1 = np.array([2,3,4,5],'int8')

# 2D array - 2 rows and 3 columns
a2 = np.array([[1,2,3],[4,5,6]])

# 3D array - 1 block, 2 rows, 4 columns
a3 = np.array([[[1,3,4,5],[3,4,5,6]]])



# 2x2 array filled with zeros

a4 = np.zeros((2,2))

# 3x3 array filled with ones
a5 =  np.ones((3,3))

# arange works like range() -> (start, stop, step)
# stop is not included, so this gives 0 2 4 6 8

a6 = np.arange(0,10,2)

# make an array from a string, each letter becomes one item
a7 = np.fromiter("jeyaram",dtype="U4")

# empty() does not set values, so you get whatever junk is in memory
a8 = np.empty((3,4),dtype="int32")



print("# one dimension",a1)
print("# two dimension",a2)
print("# three dimension",a3)

# shape tells the size of each dimension
print("# shap of an array",a3.shape)

# dtype tells what type of data is stored
print("Data type of array :", a1.dtype)

print("# two rc array with zeros",a4)
print("# three rc array with ones",a5)


print("# range of values with step",a6)

# pick one item by index, for 2D give [row, column]
print("# access via index in a1", a1[2])
print("# access via index in a2", a2[1,2])


# slicing - a2[1:2] gives row 1, a2[:,1] gives column 1 from every row
print("# access via slicing 1 row in a2", a2[1:2])
print("# access via slicing  all rwo second column in a2", a2[:,1])

print("#text array",a7,a7.dtype)

# size tells the total number of items (3 x 4 = 12)
print("# created empty array with random values",a8,a8.size)
