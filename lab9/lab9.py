"""
Tess Owens
April 24, condition statement
"""
print("\n------example 1: if statement ----------")

age = 20
agecode = 123

if age>= 21:
    print("you are an adult!")
    agecode = 200
else: 
    print("You are under 21!")
    agecode = 100


print(f"After the 'if' statement, agecode = {agecode}")    

print("\n------example 3: if statement ----------")

age = 20

if 0 <= age < 21:
    print("You are minor!")
elif 21 <= age < 65:
    print("you are an adult!")
elif 65 <= age <= 130:
    print("You are a senior citizen!")
else:
    print("unable to read age ")

print("\n------example 4: 'and' operator ----------")
temperature = 80
humidity = 100

if 70 <= temperature <= 90 and humidity < 80:
    print("the weather is pleasant")
else:
    print("The weatehr is not ideal")

print("\n------example 5: 'or' operator ----------")

day = "Monday"
is_holiday = False

if day =="Saturday" or day =="Sunday" or is_holiday:
    print("You can relax today")
else:
    print("It is a workday")

print("\n------example 6: nested condition statement ----------")

number = int(input("Enter a number:  "))
if (number>=0):
    if number==0:
        print("number is Zero")
    else:   
        print(f"{number} is positive")
else:
    print(f" {number} is negative" )


print("\n------Lab Exercise")

def gpa():
   print ("Calculate Your GPA below")
   grade1 = float(input("Enter your 1st scores: "))
   grade2 = float(input("Enter your 2nd scores: "))

   average = (grade1 + grade2) / 2
   if 90 <= average <= 100:
      grade = "A"
   elif 70 <= average <= 89.99:
      grade = "B"
   elif 60 <= average <= 69.99:
      grade = "C"
   elif 0 <= average <= 59.99:
      grade = "Fail"
   else:
      grade = "UNDEFINED"
              
        
   print(f"For the average of {round(average)}, your GPA is {grade} ")
gpa()




