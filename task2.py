#convert tuple into list
import math

a=("hello","mr","how","are","u",1)
b=list(a)
print(b)

#Write a program to calculate direction and magnitude of the vector described by the following points.
A = (20,30)
B = (30,40)
magnitude_= math.sqrt(((B[0]-A[0])**2)+((B[1]-A[1])**2))
direction=math.atan((B[1]-A[1])/(B[0]-A[0]))
print(direction)
print(magnitude_)



#Write a program to demonstrate data types that can be elements of a tuple.
for datas in a:
    print(type(datas))
