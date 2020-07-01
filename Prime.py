def isPrime(n):
    for d in range(2,n):
        if (n % d == 0):
            break
        else:
            return True
    
    return False

def primeFrom2ToN(n):
    for k in range(2,n + 1):
        prime = isPrime(k)
        if(prime):
            print(k)

primeFrom2ToN(15)

