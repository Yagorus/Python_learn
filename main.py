# all data types
"""""
text = "Hello world" 
number = 12.5
isTrue = True
lst = [ 4, 3.2, "Hello World", -1, True ]
bts = bytes(5)
bts2 = b"Hello World" 
"""""

# Conditionals
# a = 6
# b = 6

# if (a > b):
#     print("a bigger then b")
# elif a < b:
#     print("b bigger then a")
# else:
#     print("a and b equal")

# While loop

# a = 5

# while a > 0:
#     if a==3:
#         a-=1
#         break
#         #continue
#     print(a)
#     a-=1

# For loop

# lst = [ 4, 3.2, "Hello World", -1, True ]

# for item in range(2,100):
#     print(item)

#  Index


# lst = [5, 6, 7, "Hello world"]
# lst[1:3] = [1,2,3,4,5,6]
# lst.insert(2, "Hello")
# lst.append("fox")
# lstSecond = [6,2,7,123,6]
# lst.extend(lstSecond)
# lst.remove("Hello world")
# lst.pop(-2)
# # lst.clear() #clear all list
# # print(lst[:])
# print(str(len(lst)) + " Len of lst")
# # lst = [6,2,7,123,6]
# # lst.sort()

# lst1 = lst.copy() # add command .copy is important cuz it lst1 create reference to lst, so when we want to change lst1, we will change lst without .copy
# lst1[0] = "IT"

# print(lst + lst1)
# # for item in lst:
# #     print(item)


# Tuples




# tpl = ("MAC", "WINDOWS", "LINUX")

# (work, home, friend) = tpl
# print(home)
# print(work)
# print(friend)

### Change tuple 
# print(tpl[0])
# tpl = list(tpl)
# tpl.append("Arch")
# tpl = tuple(tpl)
# print(tpl)


# Set

# st = {"macos", "linux", "macos", "windows", "linux", "windows"}
#print (st)
#output
#{'linux', 'macos', 'windows'}

# print("macos" in st)
#   output
# True

# st.add("arch")
# print(st)
#   output
# {'linux', 'macos', 'windows', 'arch'}

# st.remove("windows")
# print(st)
#   output
# {'linux', 'macos'}

# st.remove("windows")
# st.remove("windows")
# print(st)
#   output
# Traceback (most recent call last):
#   File "d:\Python_learn\main.py", line 108, in <module>
#     st.remove("windows")
# KeyError: 'windows'

# st.discard("windows")
# st.discard("windows")
# print(st)
#   output
# {'macos', 'linux'}

# Dictionars

# dict = {
#     "HDD": "4G",
#     "CPU": "INTEL",
#     "RAM":  "8G"
# }

# print(dict)
# {'HDD': '4G', 'CPU': 'INTEL', 'RAM': '8G'}

# print(dict["HDD"])
# 4G

# dict["HDD"] = "5TB"
# print(dict["HDD"])
# 5TB

# dict["year"] = 2001
# print(dict["year"])
# 2001

# dict.pop("CPU")
# print(dict)
# {'HDD': '4G', 'RAM': '8G'}

# for key in dict.keys():
#     print(key)
# HDD
# CPU
# RAM
#============================================= .format() ====================================================#  
# print('This is a string {}'.format("INSERDER"))
# print('This is a string {} {} {}'.format("INSERDER1", "inserted2", "Inserted3"))
# print('This is a string {1} {2} {0}'.format("INSERDER1", "inserted2", "Inserted3"))
# print('This is a string {1} {1} {1}'.format("INSERDER1", "inserted2", "Inserted3"))
# print('This is a string {f1} {f3} {f2}'.format( f1="INSERDER1",f2= "inserted2",f3= "Inserted3"))
# Output
# This is a string INSERDER
# This is a string INSERDER1 inserted2 Inserted3
# This is a string inserted2 Inserted3 INSERDER1
# This is a string inserted2 inserted2 inserted2
# This is a string INSERDER1 Inserted3 inserted2

# print('This is a string {f:1.3} {f:0.2} {f:40.10}'.format(f= 100/70))
# This is a string 1.43 1.4 /_______this_is__^___this_number/ 1.428571429

#============================================= .format() ====================================================#

#============================================= f-string literal =============================================#
# for python 3.6

# name = "jose"
# print(f"Hello {name}")

# Hello jose
#============================================= f-string literal =============================================#
#============================================= Dictionary ===================================================#

# my_dict = {
#     "k1":"value1",
#     "k2":"value2",
#     "k3":"value3",
#     "k4":"value4",
#     "k5":"value5"
# }
# print(my_dict["k1"])
# # value1
# print(my_dict)
# # {'k1': 'value1', 'k2': 'value2', 'k3': 'value3', 'k4': 'value4', 'k5': 'value5'}

# my_dict2 = {
#     "k1":123,
#     "k2":1.24,
#     "k3":["value1","value2","value3","value4","value5"],
#     "k4":{"key4.1" : "value4.1", "key4.2":"value4.2" },
#     "k5":"value5"
# }

# print(my_dict2["k4"]["key4.2"])
# # value4.2

# my_dict3 = {
#     "k1":"value1",
#     "k2":"value2",
#     "k3":"value3",
#     "k4":"value4",
#     "k5":"value5"
# }

# print(my_dict3)
# # {'k1': 'value1', 'k2': 'value2', 'k3': 'value3', 'k4': 'value4', 'k5': 'value5'}

# # add new elemnt in dict
# my_dict3["k6"] = "value6"

# print(my_dict3)                                                                   #<=new element=>#
# # {'k1': 'value1', 'k2': 'value2', 'k3': 'value3', 'k4': 'value4', 'k5': 'value5', 'k6': 'value6'}


# my_dict3["k2"] = "another value"
# print(my_dict3)     #<==change value===>   
# # {'k1': 'value1', 'k2': 'another value', 'k3': 'value3', 'k4': 'value4', 'k5': 'value5', 'k6': 'value6'}      

# print(my_dict3.keys()) #return tuples
# # dict_keys(['k1', 'k2', 'k3', 'k4', 'k5', 'k6'])

# print(my_dict3.values())  #return tuples
# # dict_values(['value1', 'another value', 'value3', 'value4', 'value5', 'value6'])

# print(my_dict3.items()) ##return tuples
# dict_items([('k1', 'value1'), ('k2', 'another value'), ('k3', 'value3'), ('k4', 'value4'), ('k5', 'value5'), ('k6', 'value6')])
#============================================= Dictionary ===================================================#


#============================================= Tuples ===================================================#

# #tuples are immutability - cant be changed

# t1 = (1,2,3,4)
# print(t1)
# # (1, 2, 3, 4)
# t2 = (1,2,"string")
# print(t2)
# # (1, 2, 'string')
# print(t2[2])
# # string
#     # 0,1,2,3,4,5,6,7,8,9,10,11
# t3 = (1,1,1,1,1,4,6,2,2,2,21,2)
# print(t3.count(1)) 
# # 5
# print(t3.index(21)) # show first element's index
# # 10   
# # print(t3.index(3)) # show first element's index
# # ValueError: tuple.index(x): x not in tuple   

# # t3[2] = 3
# # TypeError: 'tuple' object does not support item assignmen

#============================================= Tuples ===================================================#


#============================================= Sets =====================================================#

 #Sets are unordered collection of unique elements

# st = set()
# print(st)
# # set() - empty set

# st.add(1)
# print(st) 
# # {1}  - it's not a dictionary



# st.add(1)
# st.add(2)
# print(st) # accept only uniqe values
# # {1, 2}
# lst = [1,1,1,1,1,1,2,1,12,2,2,2,2,3,23,3,3,3,3,1,323,123,1,2312,3,1]
# print(set(lst)) # do not ordered!!!
# # {1, 2, 3, 323, 2312, 12, 23, 123}

#============================================= Sets =====================================================#

