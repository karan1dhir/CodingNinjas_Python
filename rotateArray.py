def rotate(arr, n, d):
    #Your code goes here
      length = len(arr)
      for start in range(0,length//2):
        arr[start] , arr[length - start -1] = arr[length - start -1] ,arr[start]   
    
      for start in range(0,(length-d)//2):
        arr[start] , arr[(length-d) - start -1] = arr[(length-d) - start -1] ,arr[start]  

        lastIndex = length - 1
        startIndex = 0
        for start in range(length-d,length,1):
          arr[start], arr[lastIndex - startIndex] = arr[lastIndex - startIndex] , arr[start]
          startIndex += 1

arr = [1,5,3,7,2,6,0]
n = 7
rotate(arr,n,2)
print(arr)      