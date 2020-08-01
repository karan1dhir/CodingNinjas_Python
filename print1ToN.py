def print1_N(n):
    if n == 0:
        return
    print1_N(n-1)
    print(n)   

def printN_1(n):
    if n == 0:
        return
    print(n)    
    printN_1(n-1)    


n = int(input())
output = print1_N(n)
print(output)

output = printN_1(n)
print(output)