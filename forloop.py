# Multiply following matrices

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
B = [[111,22,33],
     [44,55,56],
     [47,86,19]]
C = [[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

for items in C:
    print(items)


#Multiply following matrices
C = [[111,22,33,44],
     [44,55,56,1],
     [47,86,19,2],
     [1,2,22,3]]
D = [[11,22,3,4],
     [4,5,6,1],
     [7,6,19,2],
     [1,2,22,3]]
A = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]
for i in range(len(C)):
    for j in range(len(D[0])):
        for k in range(len(D)):
            A[i][j] += C[i][k] * D[k][j]
for items in A:
    print(items)


# or it can be done by importing numpy module


import numpy
a = numpy.array([[111,22,33,44],[44,55,56,1],[47,86,19,2],[1,2,22,3]])
b = numpy.array([[11,22,3,4],[4,5,6,1],[7,6,19,2],[1,2,22,3]])
m = a.dot(b)
print(m)

# Generate the following patterns using for loop
a = 1
for i in range(1,7):
    for j in range(a):
        print("F",end="")
    a=a+2

    print()


# question B

nterms = 9
a =""
b ="F"
print("Fibonacci sequence:")
for i in range (9):
    print(b)
    Var1 = a + b
    a = b
    b = Var1

