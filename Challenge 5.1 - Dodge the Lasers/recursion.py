from math import floor,sqrt

def answer(str_n):
    
    def S(a,k):
        m = floor(a*k)
        if m <= 0:
            return 0
        n = floor((a-1)*k)
        return m*(m+1)/2 - S((1-(a**-1))**-1,n)
    
    
    return str(S(sqrt(2),int(str_n)))
