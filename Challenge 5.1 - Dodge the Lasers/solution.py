from math import floor,sqrt
from decimal import Decimal,getcontext

# With help from StackExchange
# https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s?newreg=08f205df74404edeab50f938618b3e07
# https://math.stackexchange.com/questions/2307399/solve-summation-sum-i-1n-lfloor-e-cdot-i-rfloor/2307822#2307822

def answer(str_n):
    
    getcontext().prec = 101
    a = (Decimal(2).sqrt()-1) * 10**101
    r = 0
    n = int(str_n)
    s = [(n,1)]
    
    while s:
        n,i = s.pop()
        if n <= 0:
            break
        n2 = int((a*n)//(10**101))
        r += i * (n*n2 + n*(n+1)/2 - n2*(n2+1)/2)
        s.append((n2, i * -1))
    
    return str(int(r))
        
