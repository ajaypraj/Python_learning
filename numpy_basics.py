import numpy as np
"""
Numpy is python library for array handling.
Rank is called as ==Dimension of an array
Creating numpy array

pip install numpy or 
python -m pip install numpy
"""
# 1. Creating array using list
arr=np.array([1,2,3,4])
print("Array with Rank 1",arr)

# Creating a two dimensional Array in Numpy

arr2=np.array([[1,2,3,4],[5,6,7,8]])
print("Array with Rank 2", arr2)

# 2. Creating an array from numpy tuple

arr3=np.array((1,2,3))
print("Arary created from tuple", arr3)



# # Slicing in Numpy array
# # Slicing in similar to slicing in Python list

arr4=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr4[:2,:2])  # will print first row and first columnn element so only 1 will be printed


# # Printing the array Information 
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

# Unary operation on array
arr=np.array([[1,20,3],[4,3,4],[4,1,2]])
print("Largest Element is ", arr.max())
print("row wise maximum element is ", arr.max(axis=1))
print("Coulmn wise maximum element is ", arr.max(axis=0))
print("Sum of all element is ", arr.sum())
print("Sum of element along row is ", arr.sum(axis=1))


# How to perform math operation like addition, subtraction, multiplication in numpy

# Define two numpy arrays
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.array([[1,2,1],[2,1,3],[1,2,1]])

# addition
print("Addition",arr1 + arr2)

# Subtraction
print("Subtration",arr1 + arr2)

# Multiplication
print("Multiplication",arr1*arr2)

# finding the sum of array element
print("Sum",np.sum(arr1))

# find squareroot of each element
print("Sqrt",np.sqrt(arr1))

# Transpose of an array 
print("Transpose",arr1.T)


# flatten method and ravel method
# let take a matrix and flateen the matix 
a=np.array([(1,2,3,4),(1,3,2,5)])
x=a.flatten()
print("Flattened Matrix",x)

# lets change the element of flatten matrix and see the impact on original matrix
x[2]=111
print(x)
print(a)
# Flatten matrix's lelemnt will be chnages and original matrix wll not change . It shows that 
# we have flatten matrix is deep copy of matrix a 

# lets see the same example with ravel matrix
# Here flatten matrix will be shallow copy of original matrix 

y=a.ravel()
print(y)
y[1]=11
print("original matrix a",a )
print("Flatten matrix y",y)









