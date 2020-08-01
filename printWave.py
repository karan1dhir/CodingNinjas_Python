def wavePrint(mat, nRows, mCols):
    #Your code goes here
    for i in range(mCols):
        if i %2 == 0:
            for j in range(nRows):
                print(mat[j][i],end=' ')
        else:
            k = nRows -1
            while k >= 0:
                print(mat[k][i],end=' ')
                k = k - 1

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
rows = 3
columns = 4
wavePrint(mat,rows,columns)
