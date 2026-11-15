import numpy as np

#one dimention array
oned = np.array([10, 20, 30, 40, 50])

#two dimention array matrix
twod = np.array([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ])

#three dimention array cube
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



#access based on index in one d
print("access zeroth index",oned[0])

print("access negative index",oned[-1])


#access based on row and column index in two d
#first row second column
print("access first row second column index",twod[1,2])


#for three dimenion access based on depth, row ,column

print(" access first twod matrix as depth, row, column",threed[1,1,2])

#slice based indexing

print(" Slice based indexing in oned",oned[1:4])

print("Slice based indexin in twod",twod[1:2,0:])

print("Slice based indexin multi",threed[1:2,0:2,2])


#boolean based indexing

print("Boolean based condition",oned[oned > 20])

# boolean based indexing with multiple condition

print("Boolean based index with multiple condition",oned[(oned > 20) & (oned<40)])


## fancy indexing


