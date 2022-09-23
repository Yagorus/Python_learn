def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        print(i)
        result.append(s[i:i+1])
        
    return result


# print(solution("asdfadsd"))


strings = "asdfjklasdfjklfhqwehfjlnm"
print(strings[0:2])

