def invert(lst):
     return [ -i for i in lst ]



print(invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5])
print(invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5])
print(invert([]) == [])