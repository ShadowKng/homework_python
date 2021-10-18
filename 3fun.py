import string

def counter(text):
    d = {}
    for ch in string.ascii_letters:
         d[ch]=text.count(ch)
    return d
print(counter("slatt"))