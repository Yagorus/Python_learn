myfile = open("file1.txt")
print(myfile)
# <_io.TextIOWrapper name='file1.txt' mode='r' encoding='cp1251'>

print(myfile.read())

#Print file

# Some random text
# this is text file
# for check how does work IO in python

print(myfile.read())
# It's return empty string
# The reason why it happend that coursor was at end of the file
# 
# Some random text
# this is text file
# for check how does work IO in python $ <== point at coursor
# 

print(myfile.seek(0)) # back coursor at the begining of the file    
# 0

# print(myfile.read()) # it again return me content of the file 

print(myfile.readlines()) # return list of objects
# ['Some random text\n', 'this is text file \n', 'for check how does work IO in python\n']

print(myfile.readlines()) # the same as read() 
# [] 
print(myfile.close()) # So it's important to close file after you work with? to evoid errors later on
# None

#This way we can stop think about close() file when we opened it
with open("file1.txt") as opened_file:
    content = opened_file.read()

print(content)
# Some random text
# this is text file
# for check how does work IO in python



# mode="r" - read only
# mode="w" - is write only (will overwrite files or create new!) 
# mode="a" - append only (will add on to file)
# mode="r+" - is reading or writing  
# mode="w+" - is writing and reading (Overwrites existing files or creates a new file!)

# mode by default = 'r' (read)

# with open("file1.txt",mode='w') as opened_file:
#     content = opened_file.read() 

# io.UnsupportedOperation: not readabl

#I want create new file "file2.txt"
with open("file2.txt", mode = 'w') as opened_file:
    opened_file.write("New line")
#New line

#There is files in dir "io" where new file was put

with open("file2.txt", mode = 'a') as opened_file:
    opened_file.write("\n and another line")
# New line
#  and another line
