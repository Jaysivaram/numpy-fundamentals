import numpy as np

# Create arrays
# 1D arrays (4 items each)
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# 2D arrays (2 rows, 4 columns)
arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# 3D arrays (2 x 2 x 2)
arr5 = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]]])

arr6 = np.array([[[10, 20], [30, 40]],
                 [[50, 60], [70, 80]]])


# stack: join arrays by adding a NEW dimension
# all arrays must have the same shape
# axis tells where the new dimension goes:
#   axis=0  -> put whole arrays one after another (as rows)
#   axis=1  -> pair items at the same position (as columns)
#   axis=-1 -> the last position (pairs the single items)


# 1D example: result is 2D
newarr1 = np.stack((arr1, arr2), axis=0)  # shape (2, 4): arr1 is row 1, arr2 is row 2
newarr2 = np.stack((arr1, arr2), axis=1)  # shape (4, 2): [1,5], [2,6], [3,7], [4,8]

print("1D stack, axis=0 (as rows):\n", newarr1)
print("1D stack, axis=1 (as columns):\n", newarr2)


# 2D example: result is 3D
newarr3 = np.stack((arr3, arr4), axis=0)   # shape (2, 2, 4): arr3 first, then arr4
newarr4 = np.stack((arr4, arr4), axis=1)   # shape (2, 2, 4): pairs matching rows
newarr5 = np.stack((arr4, arr4), axis=-1)  # shape (2, 4, 2): pairs matching numbers

print("2D stack, axis=0 (whole arrays):\n", newarr3)
print("2D stack, axis=1 (pair rows):\n", newarr4)
print("2D stack, axis=-1 (pair numbers):\n", newarr5)


# 3D example: result is 4D
# every axis gives shape (2, 2, 2, 2), but the values are grouped differently
newarr6 = np.stack((arr5, arr6), axis=0)  # whole arrays
newarr7 = np.stack((arr5, arr6), axis=1)  # pair matching 2x2 blocks
newarr8 = np.stack((arr5, arr6), axis=2)  # pair matching rows
newarr9 = np.stack((arr5, arr6), axis=3)  # pair matching numbers (same as axis=-1)

print("3D stack, axis=0 (whole arrays):\n", newarr6)
print("3D stack, axis=1 (pair blocks):\n", newarr7)
print("3D stack, axis=2 (pair rows):\n", newarr8)
print("3D stack, axis=3 (pair numbers):\n", newarr9)


# split: break one array into smaller arrays
# it is the opposite of stack

# Arrays to split
sarr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])      # 12 items
sarr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])  # 13 items

varr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # 4 rows, 3 columns
harr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])    # 3 rows, 4 columns
darr = np.arange(24).reshape((2, 3, 4))                           # 3D: 2 x 3 x 4


# split: equal parts only (12 items -> two parts of 6)
print("split:\n", np.split(sarr1, 2))

# array_split: parts can be uneven (13 items -> 7 and 6)
# the extra item goes to the first part
print("uneven split:\n", np.array_split(sarr2, 2))

# vsplit: split by rows (top / bottom)
print("vertical split (rows):\n", np.vsplit(varr, 2))

# hsplit: split by columns (left / right)
print("horizontal split (columns):\n", np.hsplit(harr, 2))

# dsplit: split by depth (the last axis, 4 -> 2 and 2)
print("depth split (last axis):\n", np.dsplit(darr, 2))