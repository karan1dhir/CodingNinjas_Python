
def linear_search(li,element):
    isFound = False
    for index in range(0,len(li)):
        if li[index] == element:
            isFound = True
            return index
    if isFound is False:
        return -1 

list = [1,2,3,6,5]
index = linear_search(list,6)
print(index)