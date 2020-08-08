def merge(arr1, arr2 , arr) : 
    #Your code goes here
    index1 = 0
    index2 = 0
    index3 = 0
    n = len(arr1)
    m = len(arr2)
    while index1 < n and index2 < m:
        if(arr1[index1] >= arr2[index2]):
            arr[index3] = arr2[index2]
            index2 += 1
            index3 += 1
        else:
            arr[index3] = arr1[index1]
            index1 += 1
            index3 += 1
    if(index1 < n):
        while index1 < n:
            arr[index3] = arr1[index1]
            index1 += 1
            index3 += 1
    if(index2 < m):
        while index2 < m:
            arr[index3] = arr2[index2]
            index2 += 1
            index3 += 1
     
def mergeSort(arr, start, end):
    # Please add your code here
    if len(arr) == 0 or len(arr) == 1:
        return
    
    mid = len(arr)//2
    s1 = arr[0:mid]
    s2 = arr[mid:]
    
    mergeSort(s1,start,end)
    mergeSort(s2,start,end)
    merge(s1,s2,arr)
    
        
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)
