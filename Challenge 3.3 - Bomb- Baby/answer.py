def check(m, f):
    if f == m != 1:
        return True
    if f == 0 or m ==0:
        return True

def answer(M,F):
    count = 0
    m = long(M)
    f = long(F)
    while(m + f > 2):
        if m > f:
            n = (m - f)/f + 1
            if f == 1:
                n -= 1
            count += n
            m = m - (n * f)
        if check(m,f):
            return 'impossible'
        if f > m:
            n = (f - m)/m + 1
            if m == 1:
                n -= 1
            count += n
            f = f - (n * m)
        if check(m,f):
            return 'impossible'
    if m == f == 1:
        return str(count)
    else:
        return 'impossible'
