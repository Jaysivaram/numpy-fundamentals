import numpy as np


# Create arrays
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr3 = np.array([1, 2, 3, 4, 5])


# reshape: change the shape without changing the values
# total number of items must stay the same (8 items -> 2x2x2 or 2x4)

print("reshape to 3D array:\n", arr1.reshape(2, 2, 2))

print("reshape to 2D array:\n", arr1.reshape(2, 4))

# -1 means "numpy, work out this size for me"
print("Auto size with -1:\n", arr1.reshape(2, -1))


# resize: change the shape AND the number of items
# if the new shape needs more items -> adds 0s at the end
# if the new shape needs fewer items -> drops the extra items
# note: arr.resize() changes the array itself (in place)

arr2.resize((3, 4))  # 9 items -> 12 items, adds three 0s
arr3.resize((2, 2))  # 5 items -> 4 items, drops the last one

print("Resize bigger (adds 0s):\n", arr2)

print("Resize smaller (drops items):\n", arr3)
