def digitize(n):
    n = list(str(n))[::-1]
    return [int(x) for x in n] 

# print(digitize(35231))

# 35231 => [1,3,2,5,3]
# 0 => [0]

def func(n):
    result = map(int, str(n)[::-1])
    return result
print(func(35231))