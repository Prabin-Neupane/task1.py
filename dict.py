
# Make a dictionary using lists above and delete the key-value (students:marks) pairs with lowest marks.
import math
students = ['jack','jill','david','silva','ronaldo']
marks = ['55','60','53','66','76']
dict ={}
for key in range(len(students)):
    dict[students[key]] = marks[key]
print(dict)
dict_2 ={}

for items in range(len(students)):
    dict_2[students[items]] = marks[items]
    if marks[items] == min(marks):
        del dict_2[students[items]]
    continue
print(dict_2)


# Make two lists from above dictionary


euro = {'france':5,'germany':2,'portugal':3,'hungary':6}
keys =[]
values =[]
for key,value in euro.items():
    keys.append(key)
    values.append(value)
print(keys)
print(values)



# Make two lists from above dictionary

users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
        'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
        'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}
usrnme =[]
name =[]
age = []
poison =[]
for keys,values in users.items():
    usrnme.append(keys)
    name.append(values['name'])
    age.append(values['age'])
    poison.append(values['poison'].lower())


usrnme.sort()
name.sort()
age.sort()
poison.sort()
print(name)
print(usrnme)
print(age)
print(poison)


# Create an empty dictionary called milk_carton. Add the following key/value pairs.You can make up the values or use
# a real milk carton.
# Expiration_date: a tuple with day, month, year
#  Vol: volume of milk
# Cost: cost of milk
# Brand_name
milk_carton ={}
mytuple = ("22","12",2020)
milk_carton['Expiration_date'] =(mytuple[0]+'/'+mytuple[1],mytuple[2])
milk_carton['volume_of_milk'] = 20
milk_carton['cost'] = 1200
milk_carton['brand_name'] = "amul"
print(milk_carton)



#Print out the values of all of the elements of the milk_carton using the values in the dictionary.
for key,values in milk_carton:
    print(values)

print("cost of six cartoons in {}".format(milk_carton['cost'] * 6))

