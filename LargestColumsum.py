
def lar_Col_Sum(li):
    rows = len(li)
    cols = len(li[0])
    max_sum = -1
    max_Col_Index = -1
    for i in range(cols):
        sum = 0
        for ele in li:
            sum += ele[i]
        if sum > max_sum:
            max_Col_Index = i 
            max_sum = sum
    return max_sum,max_Col_Index           

li = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
max_sum,lar_col_Index = lar_Col_Sum(li)
print(max_sum,lar_col_Index);