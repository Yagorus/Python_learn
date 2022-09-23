def solution(string, ending):
    return ending in string[len(string)-len(ending):]

def solution(string, ending):
    return string.endswith(ending)

# message = 'Python is fun'

# check if the message ends with fun
# print(message.endswith('fun'))

# Output: True    

print(solution('abcde', 'cde'), True)
print(solution('abcde', 'abc'), False)
print(solution('abcde', ''), True)