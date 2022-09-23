def get_sum(a,b):
    if a<b:
        return sum(list(range(a,b+1)))
    else:
        return sum(list(range(b,a+1)))
     
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2
# https://www.programiz.com/python-programming/methods/built-in/abs

print(get_sum(0,1))
print(get_sum(-20,20))
print(get_sum(0,-1))