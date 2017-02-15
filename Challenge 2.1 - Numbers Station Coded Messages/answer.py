def answer(l, t):
    current = start_i = 0
    for end_i in range(len(l)):
        current = sum(l[start_i:end_i+1])
        while (current >t):
            current = current - l[start_i]
            start_i +=1
        if current == t:
            return [start_i, end_i]
    return [-1,-1]
