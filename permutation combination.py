#Write a Python code to calculate Permutation (5,3)
#Write a Python code to calculate Combination (15,3)

import math
import random

permutation = int(math.perm(5,3))
combination = int(math.comb(15,3))
print( "permutation is {} ".format(permutation))
print( "combination is {} ".format(combination))


#Write a Python code that takes the degree as input from the user and convert it into radian.
degree = float((input("enter angle in degress:")))
radian = float(math.radians(degree))

print("\nangle in radian is {}".format(radian))

#Write a Python code that inputs input from the user and calculate its square root.

number = float(input("enter a number "))
squareroot = float(math.sqrt(number))
if number<0:
    print("squareroot cannot be calculate")
else:
    print ("\nsquareroot is {}".format(squareroot))

#Write a Python code to calculate LCM of (25,55)
lcm = int(math.lcm(25,55))
print("lcm is {}".format(lcm))

#Ask enter to enter two numbers (say, a and b). Generate two random numbers between those two numbers and find a combination of these two newly generated random numbers.


a=int(input("enter a numbers:"))
b=int(input("\nenter a numbers:"))

num1 =int(random.randint(a,b))
num2= int(random.randint(a,b))

comb = math.comb(num1,num2)
print(num1)
print(num2)
print("\ncombination is {}".format(comb))

#Divide 1000 by 3 and print the answer with only 5 numbers after decimal.
num = 1000/3
print(format(num,".5f"))
#Write a program to convert 108 to binary.
#Write a program to convert 1008 to hexadecimal.
a=bin(108)
b=hex(1008)
print (a)
print(b)





