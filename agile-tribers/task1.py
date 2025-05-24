#task 1
import numpy as np
n1=np.array([1,2,3,4,5,6,7,8])
print("Array is:",n1)
print("Data Type is:",n1.dtype)

import numpy as np
n1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array is:",n1)
print("shape:",n1.shape)
print("Data type is:",n1.dtype)

#task2

#arange
import numpy as np
n1=np.arange(1,10,2)
print(n1)

#zeros and ones
import numpy as np
n1=np.zeros([1,3],dtype='int32')
print("Matrix of 1D:",n1)
print()
n2=np.ones([10,10],dtype='int32')
print("Matrix of 10 X 10:",n2)

#linspace
import numpy as np
n1=np.linspace(1,11,num=25)
print(n1)

#identity
import numpy as np
n1=np.eye(10,dtype='int32')
print(n1)

#random
import numpy as np
n1=np.random.rand(4)
print(n1)

#randn
import numpy as np
n1=np.random.rand(2)
print(n1)

import numpy as np
n1=np.random.randn(6,6)
print(n1)

#randint
import numpy as np
n1=np.random.randint(6,size=(1,10))
print(n1)

#array
import numpy as np
n1=np.arange(0,25)
print(n1)

#random
import numpy as np
n1=np.random.randint(50,size=(1,10))
print(n1)

#shape
import numpy as np
n1=np.array([[1,2,3],[4,5,6]])
print(np.shape(n1))

#reshape
import numpy as np
n1=np.array([1,2,3,4,5,6])
print(n1.reshape(2,3))

#minimum
import numpy as np
n1=np.array([86,65,67,34,98])
print("Minimum value is:",min(n1))

#task3

#argument fn
import numpy as np
r=np.array([22,33,44])
r1=np.argmax(r)
print("Index of max value is:",r1)

#slicing
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
a[:5]=1000
print(a)

#indexing
import numpy as np
matt=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matt)

#arithemetic operations
import numpy as np
c=np.arange(1,11)
print("Addition is:",c+c)
print("Subtraction is:",c-c)
print("Multiplication is:",c*c)
print("Division is:",c/c)

#2array addition
import numpy as np
n1=np.array([1,2,3,4,5])
n2=np.array([6,7,8,9,10])
print("Addition is:",np.add(n1,n2))

#trignometric functions
import numpy as np
n1=np.array([0,np.pi/2,np.pi,2*np.pi,3*np.pi/2])
sine=np.sin(n1)
cosine=np.cos(n1)
print("Sine:",sine)
print("Cosine:",cosine)

#exponent
import numpy as np
n1=np.arange(1,11)
print(np.power(n1,2))

#square root
import numpy as np
n1=np.arange(1,11)
print(np.sqrt(n1))


#matrix multiplication
import numpy as np
mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat*mat)





















