from math import floor,sqrt

def answer(str_n):
    
    r = 0
    A = sqrt(2)
    s = [(sqrt(2),int(str_n))]
    
    while s:
        a,k = s.pop()
        if k <= 0:
            break
        m = floor(a*k)
        n = floor((a-1)*k)
        if a == A:
            r += m*(m+1)/2
        else:
            r -= m*(m+1)/2
        s.append(((1-(a**-1))**-1,n))
    
    
    return r
