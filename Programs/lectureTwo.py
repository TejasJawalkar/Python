import os
os.system("cls")

#string operation in python
#Escape Sequence characters
# \n
phrase_1= "This is my python tutorial.\nThis my second lecture on going.\n"
print(phrase_1)
# \t
phrase_1= "\tThis is my python tutorial.This my second lecture on going.\n"
print(phrase_1)

#Concatenation
firstName=input("Enter first name: ")
lastName=input("Enter last name: ")
fullName= firstName+" "+lastName
print(fullName)

#indexing on string 
phrase_1= "This is my python tutorial"
print(phrase_1[1])
print(phrase_1[15])

#slicing
phrase_1= "This is my python tutorial"
print(phrase_1[1:15])
print(phrase_1[:15])
print(phrase_1[15:len(phrase_1)])
print(phrase_1[-15:-1])
print(phrase_1[-len(phrase_1):-6])

#String functions
#len() 
phrase_1= input("Enter you statement to find the length = ")
length = len(phrase_1)
print("Length of entered string is= ", length)

#endsWith()
phrase_1= input("Enter you statement to find the length = ")
print(phrase_1.endswith("python"))

#capitalize()
phrase_1= input("Enter you statement to find the length = ")
print(phrase_1.capitalize())

#replace()
phrase_1= input("Enter you statement to find the length = ")
print(phrase_1.replace("p","a"))

#find()
phrase_1= input("Enter you statement to find the length = ")
print(phrase_1.find("from"))

#count()
phrase_1= "i am a python developer which also have knowledge of a .net core and angular."
print(phrase_1.count("A"))

##Conditional Statements
# if statement
age = int(input("Enter your age"))
if(age >= 18):
  print("You can drive a bike and car with issued license.")

#if_else statement
age = int(input("Enter your age"))
if(age >= 18):
  print("You can drive a bike and car with issued license.")
else :
  print("You cannot drive a bike and car without issuing license.")

#if_elif_else
percentage= int(input("Enter you percentae \t"))
if(percentage > 80):
  print("Grade A")
elif(percentage > 60):
  print("Grade B")
elif(percentage > 45):
  print("Grade C")
else:
  print("You are failed in your class....!")

#Nested if_else
age = int(input("Enter your age"))
if(age >= 18):
  license = input("Do you have driving license ?")
  if(license == "Yes" or license == 'yes' or license == 'y' or license == 'Y'):
      print("You can drive a bike and car with issued license.")
  else:
      print("You are old enough to ride bike and drive car but you don't hold driving license so you can't ride or drive.")
else:
  print("You cannot drive a bike and car without issuing license.")

#check no is even or odd entered by the user
number = int(input("Enter no to check whether it is even or odd"))
if(number % 2 ==0):
  print("Entered number =", number ," is even")
else:
  print("Entered number =", number ," is odd")

#check greatest not from 3 digits accepting user input
num_1 = int(input("Enter first number"))
num_2 = int(input("Enter second number"))
num_3 = int(input("Enter third number"))
if((num_1>num_2) and (num_1 > num_3)):
  print("Number 1 is greater")
elif(num_2> num_3):
  print("Number 2 is greater")
else:
  print("Number 3 is greater")

#check given no is multiple of 7 or not
number = int(input("Enter number to check is multiple of 7 or not"))
if(number % 7 == 0):
  print(number, "is multiple of 7")
else:
  print(number, "is not multiple of 7")

#check given no is multiple of 5 or not
number = int(input("Enter number to check is multiple of 7 or not"))
if(number % 5 == 0):
  print(number, "is multiple of 5")
else:
  print(number, "is not multiple of 5")