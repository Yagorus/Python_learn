# import  numpy
def maps(a):
    for i in range(0, len(a)):
        a[i]*=2
    return a


# print(maps([1, 2, 3]))

def check(a):
   return [x * 2 for x in a]
   
print(check([1,2,3]))