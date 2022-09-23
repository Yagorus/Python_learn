from unittest import result


def generate_hashtag(s):
        result = '#'+ "".join([i.capitalize() for i in s.split()]) 
        if result[0]=='#' and len(result)==1 or (len(s)>140):
            return False
        return result

def generate_hashtag(s):
    if not s or len(s)>140:
        return False
    return "#"+''.join(x.capitalize() for x in s.split(' '))    
 
    #your code here

print(generate_hashtag(''), False, 'Expected an empty string to return False')
print(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
print(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
print(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
print(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
print(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
print(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')