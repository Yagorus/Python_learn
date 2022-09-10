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

dict = {
    "HDD": "4G",
    "CPU": "INTEL",
    "RAM":  "8G"
}

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

