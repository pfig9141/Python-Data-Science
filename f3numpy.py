# -*- coding: utf-8 -*
"""
Created on Thu Jul 16 19:05:35 2020

@author: Piotr
"""

# numpy
import numpy as np
import numpy.random as rg
a = np.arange(15).reshape(3,5)
print(a)
print('a.shape ' + str(a.shape))                     # a.shape
print('a.ndim ' + str(a.ndim))                       # a.ndim
print('a.dtype.name ' + str(a.dtype.name))           # a.dtype.name
print('a.size ' + str(a.size))                       # a.size
type(a)                 # = numpy.ndarray

# array creation
b = np.array([-1,2,3],dtype='int32')

# list creation from array
c = np.array([ [1,2,1], [3,-1]])
    # => array([list([1, 2, -1]), list([3, -1])], dtype=object)
    # c.dtype.name => 'object'
    # will create a list

# complex numbers
c = np.array( [ (1,2,3), (2,1) ])       # lista
d = np.array( [ [ 1 + 0.j, -1-0.2j] , [-0.1-0.2j, -0.1-0.j] ], dtype=complex)
d = np.array( [ [0.2 + 0.j, -0.1-0.3j] , [-0.9-0.j, -1-0.j] ], dtype=complex)
    # 0.j = 0 
    # do not forget abuot commas

# an array of zeros
z1 = np.zeros( (100,100) );             # (100,100) = tuple
z2 = np.zeros( (100,100), dtype=np.int16 ); # np.int16 = numpy.int16

# numpy arange
n = np.arange(10,30,5)                  # 10,15,20,25
n = np.arange(1,10,1)                   # 1,2,3,4,5,6,7,8,9
n = np.arange(1,1.3,0.1)                # 1.0, 1.1, 1.2, 1.3

# linspace
l = np.linspace(0,1,11)                 # 0,0.1,0.2,0.3,...,1
l = np.linspace(0,99,100)               # 0,1,2,...,99
x = np.linspace(0,2*np.pi,1001)         # dx = 2*np.pi/1000
y1 = np.sin(x)                    
y2 = np.sin(np.sin(x))                  

# printing array
a = np.arange(6)                        # 1d array
print(a)
b = np.arange(24).reshape(3,8)          # 2d array
print(b)
c = np.arange(48).reshape(2,4,6)        # 3d array

# * and matrix product
A = np.array([ [2,-1,3] , [4,0,1] , [-1,-1,-1] ])
B = np.array([ [0,-1,-1], [3,2,-3] , [-3,6,6] ] )
C = A*B                                 # elementwise
C = A@B                                 # matmul

# operations on data with different write precision
b = np.linspace(0,np.pi,3,dtype='int16')
c = np.sin(b)
d = np.linspace(0,np.pi,3)
f = np.cos(d)
g = c+f                             # float64

# metody
a = rg.random((1,1024))
a.sum()
print(a.sum())                      # sum
print(a.mean())                     # mean
print(a.max())                      # max

A = np.array([[ -1,-1,-1] , [2,3,4] ])
A.sum(axis=0)
print(A.sum(axis=0))                # PO KOLUMNACH
A.sum(axis=1)
print(A.sum(axis=1))                # PO WIERSZACH

# example
np.arange(16384).reshape(512,32).sum(axis=0)

### NUMPY.ALL
# [False,False,False] => False
# [False,False,False,True] => False
# [True,True,True] => True
np.all(np.array([False,False,False]))
# ...

### NUMPY.ANY
# [True,True,True] => True
# [True,True,True,False] => True
# [False,False,False] => False

# NUMPY.CEIL






