
def BubbleSort(arr,n):
   for index1 in range(0,n): 
    for index in range(0,n- index1 - 1):
        if arr[index] > arr[index + 1]:
            arr[index] ,arr[index + 1] = arr[index + 1], arr[index]


arr = [1,5,3,7,2,6,0]
n = 7
BubbleSort(arr,n)
print(arr)