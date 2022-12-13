# Time: O(n)
# Space: O(n)

from functools import reduce

def countPrimes(n: int) -> int:
        if n <= 2:
            return 0
        count = 1
        flags = [True]*(n//2)
        flags[0] = False
        prime = 3
        while prime <= n**0.5:
            crossOf(prime,flags,n)
            prime = nextPrime(prime,flags,n)
        count = reduce(lambda c,val: c+1 if val else c, flags)
        return count+1
    
def crossOf(prime,flags,n):
        for i in range(prime*prime,n,prime):
            if i%2 != 0:
                flags[i//2] = False
    
def nextPrime(prime,flags,n):
        next = prime+2
        while next < n and not flags[next//2]:
            next+=2
        return next

print(countPrimes(10000))
        
