import math
# Write a python program to find the largest of three numbers .
num1,num2,num3 = input("enter three numbers  \n:").split()
if int(num1)>int(num2) & int(num1)>int(num3):
    print("largest num = \n",num1)
elif int(num2)>int(num3):
    print("largest num =\n",num2)
else:
    print("largest = \n",num3)

# Write a python program to check whether a character is uppercase or lowercase alphabet.
char = input("enter a character :\n " )
if char>="a" and char<="z":
    print("character is lowercase\n")
else:
    print("char is uppercase\n")

# WAP to find whether given input is number or character.
ch = input(" Enter  Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
    print("The Given Character is an Alphabet")

else:
    print("The Given Character is a Number")

#Write a program to check whether the input alphabet is vowel or not using if-else.
alp= (input("enter a alphabet")).lower()
vow =["a","e","i","o","u"]
if alp in vow:
    print("input is vowel")
else:
    print("input is consonant")

# Write a program to check whether the entered year is leap year or not.
year = int(input("enter a year"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("leap year")
else:
    print("not a leap year")

# Write a program to check if the number is Armstrong or not

num = input("enter a number")
digit =[]
for dig in str(num):
    digit.append(int(dig))
y = sum([math.pow(int(splited_num),3) for splited_num in digit])
if y == int(num) :
    print("armstrong")
else:
    print("not")

#Write a program to compute the grade from marks.
marks = int(input("enter your marks :"))
if 100>= marks >90 :
    print("grade = A")
elif 90 >= marks > 80:
    print("grade = B")
elif 80>= marks > 70:
    print("grade = C")
elif 70>= marks > 60:
    print("grade = D")
elif 60>=marks>50:
    print("grade = E")
else:
    print("grade = F")











