from calendar import c


def get_count(sentence):
    count=0
    dic = ("a","e","i","o","u")
    for i in range(0, len(sentence)):
        for a in range(0, len(dic)):
            if dic[a] == sentence[i]:
                count+=1
                break
    return count

# print(get_count("aeiou"))
# print(get_count("y"))

def get_count2(sentence):
    count=0
    dic = ("a","e","i","o","u")
    for i in sentence:
        if i in dic:
            count+=1
    return count

# print(get_count2("aeiou"))
# print(get_count2("y"))
def get_count3(inputStr):
    return sum(c in 'aeiou' for c in inputStr)
    # return sum(1 for let in inputStr if let in "aeiouAEIOU")

# print(get_count3("qwrbhnjklefrwvhjklweyuipwehuiop"))