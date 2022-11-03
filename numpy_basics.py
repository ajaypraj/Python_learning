import numpy as np
"""
Numpy is python library for array handling.
Rank is called as ==Dimension of an array
"""
arr=np.array([1,2,3,4])
print("Array with Rank 1",arr)

# Creating a two dimensional Array in Numpy

arr2=np.array([[1,2,3,4],[5,6,7,8]])
print("Array with Rank 2", arr2)

# Creating an array from numpy tuple

arr3=np.array((1,2,3,))
print("Arary created from tuple", arr3)

# Slicing in Numpy array
# Slicing in similar to slicing in Python

arr4=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr4[:1,:1])  # will print first row and first columnn element so only 1 will be printed


# Printing the array Information 
print("Type  of array",type(arr4))
print("Size of array",str(arr4.size))
print("Shape of the array", str(arr4.shape))
print("Axis of array", arr4.ndim)


# Numpy Array creation:
# We have already seen how to create array from list and tuple 
# Create numpy array from float type

float_array=np.array([[1,2,3],[4,5,6]], dtype='float')
print(float_array)

# Creating array from zeros 
zero_array=np.zeros((3,4))
print("Arary initialized with zeros", zero_array)

# creating a constant array value from full type
constant_array=np.full((3,3),6,dtype='complex')
print(constant_array)

# creating a random array using a random function
e=np.random.random((2,2))
print(e)

# generating a random one dimensional numpy with each value will be less than 1
f=np.arange(0,30,5)
print(f)

# Create a sequence of 10 values with range of 0 to 5 using linespace

f=np.linspace(0,5,10)
print(f)

# Performing reshaping and flatten operation

print(np.zeros((2,5)).reshape(5,2))
"""[[0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]]
"""

# Reshaping same matric
print(np.zeros((2,5)).reshape(5,2).flatten())


# Basic operation on elemnts of numpy arrar

a=np.array([[1,2,3],[4,5,6]], dtype='float')
print("Adding to each elemnt of array",a+1)
print("Subtracting 1 from each element", a-1)







