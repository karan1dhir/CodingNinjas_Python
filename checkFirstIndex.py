def checkFirstIndex(arr,x,startIndex):
    l = len(arr)
    if startIndex == l:
        return -1
    
    if arr[startIndex] == x:
        return startIndex

    smallAns = checkFirstIndex(arr,x,startIndex + 1)
    return smallAns   

print(checkFirstIndex([1,2,3,4,5],3,0))