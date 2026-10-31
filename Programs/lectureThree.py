import os
os.system("cls")
#List
marks = ["python",30,40,90,20,70,"tj"]
print(type(marks))
print(marks)
print(marks[0])
print(marks[3])
print(marks[len(marks)-1])

#replace value of list of 0th index value
marks[0] = "JT"
print(marks)
print(marks)

#slicing list
print(marks[2:4])
print(marks[-4:-1])
print(marks[1 : len(marks)-1 : 2])

#List Methods
#append()
list = [4,3,2,1,9]
list.append(5)
print(list)

#sort()
#ascending order sort
list.sort()
print(list)
#descending order sort
list.sort(reverse= True)
print(list)

#reverse()
list.reverse()
print(list)

#extend()
#extend list without second or other list
list.extend([11,14,12])
print(list)
#extend list with second or other list
list.extend(marks)
print(list)

#insert(index, element)
list.insert(5,8)
print(list)

#remove()
list.append(1)
list.append(2)
list.remove(1)
print(list)

#pop()
list.pop(4)
print(list)

#count()
print(list.count(2))
print(list.count(5))

#copy()
list2 = list.copy();
list2.extend([7,8,10])
print(list)
print(list2)

#clear()
list2.clear()
print(list2)

#tuples
#creating tuple with and without parentheses '()'
#with parentheses
number = (1,2,8,3,4,5,6,7,7,8,2,9,10,2)
print(number)
print(type(number))

#without parentheses
number = 1,2,8,3,4,5,6,7,7,8,2,9,10,2
print(number)
print(type(number))

#Creating tuple with single element with and without comma ','
#without comma it's type is values datatype
#return integer
number = (1)
print(type(number))
#return string
number = ("1")
print(type(number))
#return float
number= (1.10)
print(type(number))
#return boolean
number = (True)
print(type(number))

#with comma it's type is always tuple
#return tuple
number = (1,2,3)
print(type(number))
#return tuple
number = ("1","2","3")
print(type(number))
#return tuple
number= (1.10,2.10,3.10)
print(type(number))
#return tuple
number = (True,False)
print(type(number))


#tuples method
#index()
number = (1,2,8,3,4,5,6,7,7,8,2,9,10,2)
print(number.index(8))
print(number.index(8,3))

#count()
print(number.count(2))
print(number.count(8))

print("\nList")
#exersize on list and tuple
#list
#program to input from user for 3 movies he can watch and store it in list
#first way take three variable
movie =[]
nameofmovie1= input("Enter first movie name")
nameofmovie2= input("Enter second movie name")
nameofmovie3= input("Enter third movie name")
movie.append(nameofmovie1)
movie.append(nameofmovie2)
movie.append(nameofmovie3)
print(movie)
print("\n")

#second way take single variable and append 
movie =[]
nameofmovie= input("Enter first movie name")
movie.append(nameofmovie)
nameofmovie= input("Enter second movie name")
movie.append(nameofmovie)
nameofmovie= input("Enter third movie name")
movie.append(nameofmovie)
print(movie)
print("\n")

#third way use input() inside append method
movie =[]
movie.append(input("Enter first movie name"))
movie.append(input("Enter second movie name"))
movie.append(input("Enter third movie name"))
print(movie)
print("\n")

## check list element is palindrome or not
#using reverse and copy mehtod
palList1 = [1,2,1,2,4]
palList2 = palList1.copy()
palList2.reverse()
print("using reverse and copy method")
if(palList1 == palList2):
  print("List element are palindrome")
else: 
  print("List element are not palindrome")
print("\n")
#using slicing reverse
palList2 = palList1[::-1] 
print("using slicing and copy method")
if(palList1 == palList2):
  print("List element are palindrome")
else: 
  print("List element are not palindrome")
print("\n")
#program to print list data in ascending order
grades = ['A','A','F','B','D','A','C','C','D','B','A','F','A','B','D','C','A','F','B']
grades.sort()
print(grades)
print("\n")
#program to print list data in descending order
grades.sort(reverse= True)
print(grades)


#tuple
print("\nTuple")
#find count of stund with grade a in tuple
grade = ('A','A','F','B','D','A','C','C','D','B','A','F','A','B','D','C','A','F','B',)
#count
print("Student with grade 'A'= ", grade.count('A')) 
print("\n")
#