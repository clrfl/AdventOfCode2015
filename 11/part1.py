import re
from string import ascii_lowercase as asc

def inc(word, index=0):
    index = len(word) - 1 if index == 0 else index
    return inc(word[:index] + "a" + word[index + 1:], index - 1) if word[index] == "z" else word[:index] + asc[asc.find(word[index]) + 1] + word[index + 1:]

def valid(text, validity=False):
    for i in range(len(text)-2):
        validity = True if asc.find(text[i]) + 2 == asc.find(text[i + 1]) + 1 == asc.find(text[i + 2]) else validity
    validity = validity if re.match(".*(.)\\1.*(.)\\2.*", text) else False
    return False if "i" in text or "o" in text or "l" in text else validity

text = "vzbxkghz"
while not valid(text): text = inc(text)
print(text)
