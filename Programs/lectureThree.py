import os
os.system("cls")
#List
marks = ["python",30,40,90,20,70,"tj"]
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
