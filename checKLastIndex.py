def checkLastIndex(arr,x):
    l = len(arr)
    if l == 0:
        return -1

    smallList = arr[1:]
    smallAns = checkLastIndex(smallList,x)
    if smallAns == -1:
        if arr[0] == x:
            return 0 
        else:
            return -1      
    else:
        return smallAns + 1
    

def checkLastIndexBetter(arr,x,startIndex):
    l = len(arr)
    if startIndex == l:
        return -1

    smallAns = checkLastIndexBetter(arr,x,startIndex + 1)
    if smallAns == -1:
        if arr[startIndex] == x:
            return startIndex 
        else:
            return -1      
    else:
        return smallAns

print(checkLastIndexBetter([1,2,5,4,5],5,0))