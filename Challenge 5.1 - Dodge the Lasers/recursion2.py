from math import floor,sqrt

def answer(str_n):
    
    a = sqrt(2)
    
    def S(n):
        if n <= 0:
            return 0
        n2 = floor((a-1)*n)
        return n*n2 + n*(n+1)/2 - n2*(n2+1)/2 - S(n2)
    
    return str(int(S(int(str_n))))
