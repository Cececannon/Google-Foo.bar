import operator as op
from functools import reduce

def sub_answer(n_in_line, start_i):
    if n_in_line % 4 == 1:
        return n_in_line + start_i - 1
    elif n_in_line % 4 == 2:
        return 1
    elif n_in_line % 4 == 3:
        return n_in_line + start_i
    elif n_in_line % 4 == 0:
        return 0
        
def answer(s,l):
    output = []
    count = 0
    for x in range(l):
        start_i = x*l+s
        if start_i % 2 == 0:
            n_in_line = (l-count)
            output.append(sub_answer(n_in_line, start_i))
        elif start_i % 2 == 1:
            output.append(start_i)
            n_in_line = (l-count-1)
            start_i += 1
            if n_in_line > 0:
                output.append(sub_answer(n_in_line, start_i))             
        count +=1
    return reduce(op.xor, output)
