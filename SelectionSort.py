def selectionSort(arr,n):
    for index1 in range(0,n):
        for index in range(index1 + 1,n):
            if arr[index1] > arr[index] :
                arr[index1],arr[index] = arr[index],arr[index1]
                

arr = [1,5,3,7,2,6,0]
n = 7
selectionSort(arr,n)
print(arr)