def get_middle(s):
    if len(s) % 2:
        return s[len(s)//2:len(s)//2+1]
    else:
        return s[len(s)//2-1:len(s)//2+1]

print(get_middle("test"),"es")
print(get_middle("testing"),"t")
print(get_middle("middle"),"dd")
print(get_middle("A"),"A")
print(get_middle("of"),"of")