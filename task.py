import imp


import math
def main():
    vars = ask_value()
    print(discriminant(vars[0], vars[1],vars[2]))

def ask_value():
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = int(input("Enter c : "))
    return (a,b,c)

def discriminant(a,b,c):
    d = int(b*b - 4*a*c)
    x1 = (-b + math.sqrt(d))/2*a
    x2 = (-b - math.sqrt(d))/2*a
    return (x1,x2)

main()