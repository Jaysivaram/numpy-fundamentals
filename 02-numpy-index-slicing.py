import numpy as np

# 1D array - just a simple list of numbers
oned = np.array([10, 20, 30, 40, 50])

# 2D array - like a table / matrix with rows and columns
twod = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ])

# 3D array - like a cube, two 3x3 matrices stacked together
threed = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
    ])


# make a cube with numbers 0 to 23, shape is (2 depth, 3 rows, 4 columns)
cube = np.arange(24).reshape(2,3,4)

# 1D indexing - index starts from 0
print("access zeroth index",oned[0])

# negative index counts from the end, -1 is the last item
print("access negative index",oned[-1])


# 2D indexing - give [row, column]
# twod[1,2] -> row 1, column 2 (counting from 0) -> 6
print("access first row second column index",twod[1,2])


# 3D indexing - give [depth, row, column]
# threed[1,1,2] -> second matrix, row 1, column 2 -> 15
print(" access first twod matrix as depth, row, column",threed[1,1,2])

# Slicing - start:end, end is not included

# items from index 1 to 3 -> [20 30 40]
print(" Slice based indexing in oned",oned[1:4])

# only row 1, all columns
print("Slice based indexin in twod",twod[1:2,0:])

# second matrix, first two rows, column 2
print("Slice based indexin multi",threed[1:2,0:2,2])


# Boolean indexing - pick only the items where the condition is True

print("Boolean based condition",oned[oned > 20])

# for more than one condition use & (and) or | (or), wrap each condition in brackets

print("Boolean based index with multiple condition",oned[(oned > 20) & (oned<40)])


# Fancy indexing - pass a list of indexes and get those items back

index = [0,2,4]
print("Access based on array of indexes",oned[index])


# Integer array indexing - same idea, but the indexes are in a numpy array

indeces = np.array([1,3])
print("Access based on Array of indeces",oned[indeces])



# Ellipsis (...) means "take all the remaining dimensions"
# saves us from writing : again and again for big arrays

# same as cube[:, :, 1] -> column 1 from every row and depth
print("Ellipsis index for column",cube[...,1])

# same as cube[1, :, :] -> the whole second block
print("Ellipsis index for depth",cube[1,...])

# same as cube[:, 1, :] -> row 1 from every depth
print("Ellipsis index for row",cube[:,1,...])


# np.newaxis adds a new dimension
# handy to turn a 1D array into a column (or row) vector

print("oned array shape will be 5,",oned.shape)

# [:, np.newaxis] turns shape (5,) into (5,1) -> a column
newaxis = oned[:,np.newaxis]
print("convert oned array to 2d shape will be 3,1",newaxis)

print("oned array shape will be 5,1",newaxis.shape)


# We can change values using index or slice too

# index 1 gets replaced with 100
oned[1:2] = 100

print("modifed oned",oned)

# ndim tells how many dimensions the array has
print(oned.ndim)
