
from cgitb import reset
import re


def spin_words(sentence):
    return " ".join([i[::-1] if len(i) >=5 else i for i in sentence.split()])


print(spin_words("CodeWars"))
print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))