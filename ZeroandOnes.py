def sortZeroesAndOne(arr, n) :
    #Your code goes here 
    start = 0 
    end = n-1
    while start < end:
        if (arr[start] == 1 and arr[end] == 0) :
            arr[start] , arr[end] = arr[end] , arr[start]
            start += 1
            end -= 1
        if arr[start] == 0:
            start += 1
        if arr[end] == 1:
            end -= 1

arr = [0, 1, 1, 0, 1, 0, 1]
n = 7
sortZeroesAndOne(arr,n)
print(arr)