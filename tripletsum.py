def findTriplet(arr, n, x) :
    #Your code goes here
    pair = 0
    index = 0
    while index < n:
        index1 = index + 1
        while index1 < n:
            index2 = index1 + 1
            while index2 < n:
                if x == arr[index] + arr[index1] + arr[index2]:
                    pair += 1
                index2 += 1
            index1 += 1
    index += 1       
    return pair  