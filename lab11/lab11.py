''''
Tess Owens 
April 
'''
#import 'math module
import math

# import all from file "lab11_function"
from lab11_functions import *



print("\n -----Example 1: Python Dictionary------")
#create a dictionary 

car = {
    "brand" : "Ford",
    "model" : "Mustang", 
    "year"  : 1964
}

# print a complete dictionary
print(car)
# to access items in a dictionary we use [] goes the key's name
print(f"The year of the car is = {car}['year']")

#update the value of the key
car["year"] = 1980
print(f"the year of the car was update to = {car['year']}")
# add key:value pair
car["color"] = "red"
print(car)
print("\nLoop through each key in dictionary")
for k in car:
    print(car[k])
print("\nLoop through each pair in dictionary")
for k in car:
    print(f"{k} has value = {car[k]}")

print("\n----Ecample 2: Python dictionary application-------")
#given the following list, create a dictionary that will counts the numb er of times that a word appears in the string.
#Create the dictionary to organize the words as the keys, and the number of occurency of the word as the value of the key.
phrase = "to be or not to be" 
print(f"original phrase = {phrase}")
phrase_split = phrase.split()
print(f"splitted phrase = {phrase_split}")
# create the dictionary
word_count_dict ={}
#loop to each word in the list
for word in phrase_split:
    if word in word_count_dict:
        word_count_dict[word] +=1
    else: 
        word_count_dict[word] =1
# print result
print("Result of dictionary: ")
for w in word_count_dict:
    print(f"'{w}' = {word_count_dict[w]}")

print("\n----Example 3: Function that does not return values-------")
#run funtion 'greeting'
greeting()

print("\n----Ecample 4: Function with parameters-------")
#call function 'printusername'
printusername("Peter Pan")
printusername("Tess Owens")

print("\n----Ecample 5: Function with default parameters-------")
user_country("Martha", "Chile")
user_country("Anna")
user_country("","France")

print("\n------- Example 6: function with return value------")
#num1 = 2
#num2 = -6
num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))

prod1 = product(num1, num2)
print(f"The product of {num1} and {num2} is = {prod1}")
'''prod1 = product(num1)
prod1 = product(num2)
print(f"the product is = {prod1}")
prod1 = product()
print(f"The product is = {prod1}")'''

print("\n------- Example 7: Boolean function------")
checknum1 = multiple3(num1)
checknum2 = multiple3(num2)
print(f"Is {num1} multiple of 3? {checknum1}")
print(f"Is {num2} nultiple of 3? {checknum2}")

print("\n------- Example 8: composition function------")
# test collectnum()
#number = collectnum()
#print(number)
# test sumnumbers()
sumall = sumnumbers(3)
print(sumall) #(printresult)(sumnumbers(3))

print("\n -----Example 9: built-in function------")
r = 2 
a = areacircle(r)
areaprint(a,r)

print("\n -----Example 10: try-except----")
r1 = ratio_hour(0)
r2 = ratio_hour(3)
r3 = ratio_hour("Peter")

print("\n -----Example 11: CLASSES----")
#create an instant of the class
user1 = Myclass()
print(f"An instance of the class = {user1}")
# call the class property
user1id = user1.id
print(f"user 1 id = {user1id}")
#call the class method
user1msg = user1.msg()
print(f"user 1 message = {user1msg}")

print("\n -----Example 12: instantiaion classes----")
#create an instant of the class
paircomplexnumber = Complexnumber(2, 3)
#call the instance object 'r' of the class 
real = paircomplexnumber.r
print(f"The real part is {real}")

print("\n -----Example 13: classes application----")
# create an instant of the class
car1 = Car("Tesla", "S", 2023)

# call property 'odormeter_reading'
car_reading = car1.odometer_reading
print(f"Car miles reading = {car_reading}")
# call method 'get_car_description'
print(car1.get_car_description())
#call method 'read_odometer'
print(car1.read_odometer())
# update the odometer to mileage = 10
car1.update_odometer(10)
print(car1.read_odometer())
car1.update_odometer(5)
print(car1.read_odometer())

# add 20 miles to the odometer
car1.increment_odometer(20)
print(car1.read_odometer())
car1.increment_odometer()









                