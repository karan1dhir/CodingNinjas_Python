def sumOfTwoArrays(arr1, n, arr2, m, output) :
    
    #Your code goes here
    carry = 0
    endIndexarr1 = n - 1
    endIndexarr2 = m - 1
    endIndexoutput = max(n,m)
    for index in range(0,endIndexoutput + 1):
        output.append(0)
    
    while endIndexarr1 >=0 and endIndexarr2 >=0:
        num = arr1[endIndexarr1] + arr2[endIndexarr2] + carry
        if num > 9:
            output[endIndexoutput] = num % 10
            carry = num // 10
        else:
            output[endIndexoutput] = num
        endIndexoutput -= 1
        endIndexarr1 -= 1
        endIndexarr2 -= 1
       
    
    while endIndexarr1 >= 0:
        num = arr1[endIndexarr1] + carry
        if num > 9:
           output[endIndexoutput] = num % 10
           carry = num // 10
        else:
            output[endIndexoutput] = num
        endIndexoutput -= 1
        endIndexarr1 -= 1  
        
    while endIndexarr2 >= 0:
        num = arr2[endIndexarr2] + carry
        if num >9:
           output[endIndexoutput] = num % 10
           carry = num // 10
        else:
             output[endIndexoutput] = num
        endIndexoutput -= 1
        endIndexarr2 -= 1  
    output[endIndexoutput] = carry   
    

arr1 = [6,2,4]
n = 3
arr2 = [7,5,6]
m = 3
output = []
sumOfTwoArrays(arr1,n,arr2,m,output)
print(output)
