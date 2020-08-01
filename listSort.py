def is_list_sorted(a):
    l = len(a)
    if l == 0 or l == 1:
        return True
    if a[0] > a[1]:
        return False
    
    smallList = a[1:]
    isSmallerListSorted = is_list_sorted(smallList)
    return isSmallerListSorted 
       

def isSortedBetter(a,startIndex):
    l = len(a)
    if startIndex == l-1 or startIndex == l:
        return True

    if a[startIndex] > a[startIndex + 1]:
        return False

    isSmallerListSorted = isSortedBetter(a,startIndex + 1)
    return isSmallerListSorted        

arr = [1,2,3,10,5]
print(isSortedBetter(arr,0))    