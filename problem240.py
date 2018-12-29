def searchMatrix(matrix, target):
    r=0
    c=len(matrix[0])-1

    while(c>=0 and r<len(matrix)):
        #print(matrix[r][c])
        if matrix[r][c]==target:
            return True
        if matrix[r][c]<target:
            r+=1
        else:
            c-=1

    return False





print(searchMatrix([ [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]],20))