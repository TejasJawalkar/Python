import os;
os.system("cls")
print("\n")

#Dictionary
print("Dictionary in python")
print("\n")
data={
  "firstName": 'Tejas',
  "lastName": 'Jawalkar'
  }

print(data)
print(type(data))
print("\n")

#with any data type
studentInfo = { 
  "firstName": 'Tejas',
  "firstName": 'Sanjay',
  "lastName": 'Jawalkar',
  "subjects": ("C","C++","Python","Data Structure","Java"),
    "class":["BCA-I","BCA-II"]
  }
print(type(studentInfo))
print(studentInfo)
print("\n")

#Access particular value from dict
studentInfo = { 
"firstName": 'Tejas',
"lastName": 'Jawalkar',
"subjects": ("C","C++","Python","Data Structure","Java"),
"class":["BCA-I","BCA-II"],
"mobileNo": 9785676875
}

print(studentInfo["firstName"])
print(studentInfo["mobileNo"])
print("\n")

#update value of any key using key 
studentInfo = { 
"firstName": 'Tejas',
"lastName": 'Jawalkar',
"subjects": ("C","C++","Python","Data Structure","Java"),
"class":["BCA-I","BCA-II"],
"MobileNo": 9785676875
}

studentInfo["firstName"] = "Harashad"
studentInfo["lastName"] = "Mehta"
studentInfo["class"].append("MCA-I")
print(studentInfo)
print("\n")

#insert new key inside dict
studentInfo["currentClass"] = "BCA_III"
print(studentInfo)
print("\n")

#empty dictonary
studentInfor = {}
studentInfor["name"] = "Harashad"
studentInfor["surname"] = "Mehta"
print(studentInfor)
print("\n")

#nested dictonary
orderDetails = {
  "customerid":1255090,  
  "productid" : 12345,
  "userAddress": {
    "address1":"70 foot road",
    "city": "solapur",
    "pincode":413006
  },
  "paymentdetails":{
    "payemntType":"Cash on Delivery",
    "amount": 150.50,
    "currency":"INR"
  }
}

print(type(orderDetails))
print(orderDetails)

#print child data dict particular value of key
print(orderDetails["userAddress"]["address1"])
print("\n")

#inserting new child dict inside existing dict
orderDetails["customerDetails"] = {
    "mobileno":9878787877,
    "fullName":"Tejas Jawalkar"
  }
print(orderDetails)
print("\n")

#update value child key of dict
orderDetails["customerDetails"]["mobileno"] = 9172552233
print(orderDetails)
print("\n")
#comma issue with dict and list
demolist = [],
demodict = {},

print("Created with ','", type(demodict))
print("Created with ','", type(demolist))
print("\n")

#Dictionary Methods
orderDetails = {
  "customerid":1255090,  
  "productid" : 12345,
  "userAddress": {
    "address1":"70 foot road",
    "city": "solapur",
    "pincode":413006
  }
}

#keys()
print(orderDetails.keys())
print(type(orderDetails.keys())) #converted into list
print("\n")
print(list[orderDetails.keys()]) #converted into list
print(type(list[orderDetails.keys()]))
print("\n")

#values()
print(orderDetails.values())
print(type(orderDetails.values())) #converted into list
print(type(list[orderDetails.values()])) #converted into list
print("\n")

#items()
dictitems= orderDetails.items()
print(dictitems)
print("\n converting items into tuple and putting inside list")
dictitemslist = list(orderDetails.items()) #converting into list
print(dictitemslist)
print(dictitemslist[0])
print(dictitemslist[1])
print("\n")

#get(key) 
#without using get will get error and further execution happens of code
#print(orderDetails["name"])

#with specific function use we can avoid this kind of situation or errors.
print(orderDetails.get("userAddress"))
print("\n")

#update(dictionary) - it update or insert if no matching key found
#dictionary object inside update() method without dict object
orderDetails.update({"paymentType":"cash on delivery"})
print(orderDetails)
print("\n")


#dictionary object inside update() method with existing value without dict object
orderDetails.update({"gst":"13.3%"})
print(orderDetails)
print("\n")


#with new dictonary object
paymentDetails= {"paymentType":"net banking"}
orderDetails.update(paymentDetails)
print(orderDetails)
print("\n")

paymentDetails= {"paymentType":"cash on delivery", "totalPrice": 150.50, "FastDelivery":True }
orderDetails.update(paymentDetails)
print(orderDetails)
print("\n")

#pop()
orderDetails.pop("paymentType")
print(orderDetails)
print("\n")

#popitem()
result= orderDetails.popitem()
print(result)
print(orderDetails)
print("\n")

#setdefault(key,value)
#when the key given is not present it creates the key in dict
print(orderDetails)
orderDetails.setdefault("paymentType","cash on delivery")
print(orderDetails)
print("\n")
#when the key given is present it update the vlaue of key in dict
orderDetails.setdefault("paymentType","net banking")
print(orderDetails)
print("\n")

#copy()
new_orderdetails = orderDetails.copy()
new_orderdetails.update({"productid":12121212})
print(orderDetails)
print("\n")
print(new_orderdetails)
print("\n")

#fromKeys()
result = list(orderDetails.keys())
print(result)
print(orderDetails.fromkeys(result,"unknown"))
print("\n")

#clear()
print(new_orderdetails.clear())
print(new_orderdetails)
print("\n")

##Set in python
print("Set in python")
print("\n")

#creating set 
collection = {2, 1.21,"tejas",True, 1, False, 0}
print(collection)
print(type(collection))
print("\n")

#issue with {} for creating set
collection = {}
print(type(collection))

#issue is resolved using set()
collection = set()
print(type(collection))
print("\n")

#Set Methods 
collection = set()
#add(value)
collection.add(1)
collection.add(2)
collection.add(3)
collection.add((4,5,6))
print(collection)
print("\n")

#remove(value) - it gives and error if no matching found 
collection.remove(1)
print(collection)
print("\n")

#we cannot pass dictionary and list
#collection.add([4,5,6])
#collection.add({"tj","jt"})
# print("\n")

#pop()
print(collection.pop())
print("\n")

#union(set)
set1 = {1,2,3}
set2 = {2,4,5}
print(set1.union(set2))
print("\n")

#intersection(set)
set1 = {1,2,3}
set2 = {2,4,5}
print(set1.intersection(set2))
print("\n")

#discard(value) - it will remove the elemnt and will not throw an error if specified element is not present and none if not present
print(collection.discard(1))
print("\n")

#difference(set)
set1 = {1,2,3}
set2 = {2,4,5}
print(set1.difference(set2))
print("\n")

#difference_update(set)
set1 = {1,2,3,4}
set2 = {3,4,5}
set1.difference_update(set2)
print(set1)
print("\n")

#intersection_update(set)
set1 = {1,2,3,4}
set2 = {3,4,5}
set1.intersection_update(set2)
print(set1)
print("\n")

#isdisjoint(set)
set1 = {1,2,3,4}
set2 = {3,4,5}
print(set1.isdisjoint(set2))
print("\n")

#issubset(set)
set1 = {1,2,3,4}
set2 = {3,4,5}
print(set1.issubset(set2))
print("\n")

#issuperset(set)
set1 = {1,2,3,4}
set2 = {3,4,5}
print(set1.issuperset(set2))
print("\n")

#symmetric_difference(set)
set1 = {1,2,3,4}
set2 = {3,4,5}
print(set1.symmetric_difference(set2))
print("\n")


#symmetric_difference_update(set)
set1 = {1,2,3}
set2 = {3,4,5}
set1.symmetric_difference_update(set2)
print(set1)
print("\n")

#update(set)
set1 = {1,2,3,4}
set2 = {3,4,5}
set1.update(set2)
print(set1)
print("\n")

#copy
set1 = {1,2,3,4,5,5}
copy_set=set1.copy()
set2 = {4,5,7,9}
copy_set.update(set2)
print(set1)
print(set2)
print(copy_set)
print("\n")


#clear()
print(set1.clear())
print(set2.clear())
print(copy_set.clear())
print(set1)
print(set2)
print(copy_set)
print("\n")

"""store following word meaning in python dictionary
table: “a piece of furniture”, “list of facts & figures”
cat: “a small animal”"""
dictonary = {
  "table":("a piece of furniture", "list of facts & figures"),
  "cat":"a small animal" 
}
print(dictonary)
print("\n")

"""given a list of subject for student. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
  {"python", "java", "c++", "python","javascript","java", "python", "java", "c++", "c"}
"""
subjects= {"python", "java", "c++", "python","javascript","java", "python", "java", "c++", "c"}
print("Total No of classroom required by all students", len(subjects))
print("\n")

"""
  enter marks of 3 subject from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.
"""
# marks = {}
# mathmarks = float(input("\n Enter Maths mark\t"))
# chemarks = float(input("\n Enter Chemistry mark\t"))
# biomarks = float(input("\n Enter Bio mark\t"))
# allMarks = {"Maths":mathmarks, "Chemistry": chemarks, "Biology": biomarks}
# marks.update(allMarks)
# print(marks)
# print("\n")

"""
Figure out a way to store whole and decimal same number in the set.
"""
#using string and number datatype
numbers = set()
numbers.update({"9.0", 9})
print("first approach ", numbers)
print("\n")

#using tuple and value pair
value = {
  ("int",9),
  ("float",9.0)
}
numbers.clear()
numbers.update(value)
print("second approach", numbers)
print("\n")