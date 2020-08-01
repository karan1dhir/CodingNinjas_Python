def powerNumber(x,n):
    if n == 0:
        return 1    
    smallAns = powerNumber(x,n-1)
    return x * smallAns

x,n = input().split(' ')
output = powerNumber(int(x),int(n))
print(output)