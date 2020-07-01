n=5
if n%2==0:
    for i in range((n//2)):
        for j in range(n):
            print(2*n*i+j+1,end=" ")
        print()
    for i in range((n//2),0,-1):
        for j in range(n):
            print(2*n*i+j+1-n,end=" ")
        print()
else:
    for i in range((n//2)+1):
        for j in range(n):
            print(2*n*i+j+1,end=" ")
        print()
    for i in range((n//2),0,-1):
        for j in range(n):
            print(2*n*i+j+1-n,end=" ")
        print()