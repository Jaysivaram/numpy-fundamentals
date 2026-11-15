import numpy as np


#one dimention
a1 = np.array([2,3,4,5],'int8')

# two dimention
a2 = np.array([[1,2,3],[4,5,6]])

# three dimention
a3 = np.array([[[1,3,4,5],[3,4,5,6]]])



#file with zeros

a4 = np.zeros((2,2))

#file with ones
a5 =  np.ones((3,3))

#arrange the value in range with steps
# (start,endbefore,step)

a6 = np.arange(0,10,2)

#create array from text
a7 = np.fromiter("jeyaram",dtype="U4")

#create empty array with random values
a8 = np.empty((3,4),dtype="int32")



print("# one dimension",a1)
print("# two dimension",a2)
print("# three dimension",a3)

print("# shap of an array",a3.shape)

print("Data type of array :", a1.dtype)

print("# two rc array with zeros",a4)
print("# three rc array with ones",a5)


print("# range of values with step",a6)

print("# access via index in a1", a1[2])
print("# access via index in a2", a2[1,2])


print("# access via slicing 1 row in a2", a2[1:2])
print("# access via slicing  all rwo second column in a2", a2[:,1])

print("#text array",a7,a7.dtype)

print("# created empty array with random values",a8,a8.size)