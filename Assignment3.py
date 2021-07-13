# Make a list of ten students in your class. Print the name of each student whose name starts with ‘B’.
# Make a list of ten students in your class. Print the name of each student whose name ends with ‘a’.
import math
student = ["dawa", "prabin", "nabaraj", "diwas", "alish", "nirayu", "kamalshel", "shenang", "amit", "binay"]
for name in student:
    if name.upper()[0] == "B":
        print(name)

for name in student:
    if name.lower()[-1] == "a":
        print(name)
#Print all the unique elements in the following list
#fifa = ['Italy','Argentina','Germany','Brazil','France','Brazil','Italy','Spain','Germany','France']

fifa = ['Italy','Argentina','Germany','Brazil','France','Brazil','Italy','Spain','Germany','France']
for elements in fifa:
    y = fifa.count(elements)
    if y == 1:
        print(elements)


#Change the first alphabet of all elements of the following list to capital. Bob = [‘hurricane’,’tambourine’,’blowing’,’numb’]
Bob = ["hurricane","tambourine","blowing","numb"]
for elements in Bob:
    print(elements.capitalize())

# Find  A union B and A intersection B
A = set(['a','b','c','d'])
B = set(['1','a','2','b'])
print("union =",A | B)
print("intersection =",A & B)

#Calculate the mean and standard deviation of the following list:
Numbers = [1,2,3,5,88,99,55,33,41,52]
mean= (sum(Numbers)/len(Numbers))

print("mean = ",mean)
sd = []
for numbers in Numbers:
   sd.append((numbers - mean)**2)
print("SD = ", math.sqrt((sum(sd)/len(Numbers))))



