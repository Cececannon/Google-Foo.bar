import re

def f(char):
    c = ord(char.group(0))
    if c>96 and c <123:
        return chr(219-c)
    else:
        return chr(c)
 
def answer(s):
    return re.sub('.', lambda c: f(c), s)
