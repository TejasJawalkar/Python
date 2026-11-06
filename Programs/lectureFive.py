import os
os.system("cls")
#Loops

#while loop

i=1
while i <= 10:
  print(i)
  i+=2
print("\n")

#While loop practice
#print number from 1 to 100
i = 1;
while i<=100:
  print(i)
  i+=1;
print("\n")

#print number from 100 to 1
i = 100;
while i>=1:
  print(i)
  i-=1;
print("\n")

#print mulitplication table of number 'n'
n = 2 #int(input("Enter number to pring multiplication table"))
i = 1;
while i<=10:
  print(n*i)
  i+=1;
print("\n")

#print the element of following list using a loop.
list_Value = [1,4,9,16,25,36,49,64,81,100]
listlength = len(list_Value)
count = 0
while(count < listlength):
  print(list_Value[count])
  count+=1
print("\n")


#wap to search for number x in this tuple using loop
tuple_Value = (1,4,9,16,25,36,49,64,81,100,9)
no = 3 #int(input("Enter number to search \t "))
tuplelen = len(tuple_Value)
inx = 0
while(inx < tuplelen):
  if(tuple_Value[inx] == no):
    print(no,"found on index", inx)
  inx+=1
print("\n")

#Loop termination operators:
#break 
no = 0
while no <= 5:
  print(no)
  if(no == 3):
    break
  no+=1
print("\n")

# continue
i = 0
while i <= 5:
  if(i == 3):
    i+=1
    continue
  print(i)
  i+=1
print("\n")
print("for loop")
print("\n")
#for loop
no = 2;
for i in range(1 ,11):
  print(no * i);
print("\n")

#practical question on for loop
"""print the element of following list using a for loop.
[1,4,9,16,25,36,49,64,81,100]"""
nums = [1,4,9,16,25,36,49,64,81,100]
for i in nums:
  print(i)
print("\n")

"""search the element from following tuple using a for loop.
[1,4,9,16,25,36,49,64,81,100] take input from user for value to search"""

no = 5 #int(input("Enter no to search in tuple "))
nums = [1,4,9,16,25,36,49,64,81,100]
for i in nums:
  if(i==no):
    print(no, "found in tuple at index", nums.index(i))
    break;
else:
  print(no, "not found in tuple")
print("\nrange function")
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

print("\n")

print("print 1 to 100")
for i in range(1,101):
  print(i)
print("\n")


print("print 100 to 1")
for i in range(100,0,-1):
  print(i)
print("\n")

print("print multiplication of a number n")
x = 4 #int(input("Enter number"))
for i in range(1,11):
  print(x*i)
print("\n")

print("Pass Statement ")
for el in range(10):
  pass
print("\n")
#if i <= 10:
  #here it will throw an error expected an intended block after if 
#else:
# print("it will throw an error ")

# practice question
#find the sum of first n numbers using both loop
x1= int(input("Enter number"))
print("\nwhile loop\n")
sum = 0
i = 0
while i<=x1:
  sum +=i
  i +=1
print("in while loop sum of first number", sum)
print("\nfor loop\n")
sum = 0
i = 0
for i in range(1,x1+1):
  sum +=i;
print("in for loop sum of first number", sum)
print("\n")

print("find the factorial of first n number")
x= int(input("Enter number"))
fact=1
print("\nfor loop\n")
for i in range(1,x+1):
  fact = fact * i 
  print(fact)
print("\n")
