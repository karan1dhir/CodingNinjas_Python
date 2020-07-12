
def InsertionSort(arr,n):
    for i in range(1,n):
        temp = arr[i]
        j = i - 1
        while j>=0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp 



arr = [1,5,3,7,2,6,0]
n = 7
InsertionSort(arr,n)
print(arr)