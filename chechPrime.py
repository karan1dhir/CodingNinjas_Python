n = int(input())
divisor = 2
flag = False
while divisor < n:
    if n % divisor == 0:
       flag = True
       break
    divisor += 1 
if flag == True:
    print("n is not prime")
else:
    print("n is prime")           


