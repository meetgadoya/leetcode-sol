def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])

    for i in range((n // 2) + (n % 2)):
        for j in range(n // 2):
            row, col = i, j
            temp = [0] * 4
            for k in range(4):
                temp[k] = matrix[row][col]
                row, col = col, n - 1 - row
            for k in range(4):
                matrix[row][col] = temp[(k - 1) % 4]
                row, col = col, n - 1 - row



#####################################   2ND METHOD  #######################

def rotate(self, A):
    n = len(A)
    for i in range(n):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    for row in A:
        for j in range(n / 2):
            row[j], row[~j] = row[~j], row[j]