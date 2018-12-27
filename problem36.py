def isValidSudoku(board):
    n=9
    ##  for each row
    for i in range(9):
        j=board[i]
        d={}
        for k in j:
            l=ord(k)
            if l>=48 and l<=57:
                if l in d:
                    return False
                else:
                    d[l]=k
    ##  for each column
    for j in range(9):
        d={}
        for row in board:
            l=ord(row[j])
            if l>=48 and l<=57:
                if l in d:
                    return False
                else:
                    d[l]=k


    ##  checking each small square
    d={}
    for i in range(0,3):
        for j in range(0,3):
            l=ord(board[i][j])
            if l >= 48 and l <= 57:
                if l in d:
                    return False
                else:
                    d[l]=1
    d = {}
    for i in range(0,3):
        for j in range(3, 6):
            l = ord(board[i][j])
            if l >= 48 and l <= 57:
                if l in d:
                    return False
                else:
                    d[l] = 1
    d = {}
    for i in range(0,3):
        for j in range(6, 9):

            l = ord(board[i][j])
            # print(l)
            # print(board[i][j])
            # print(d)

            if l >= 48 and l <= 57:
                if l in d.keys():
                    return False
                else:
                    d[l] = l

    d={}
    for i in range(3,6):
        for j in range(0,3):
            l=ord(board[i][j])
            if l >= 48 and l <= 57:
                if l in d:
                    return False
                else:
                    d[l]=1
    d = {}
    for i in range(3,6):
        for j in range(3, 6):
            l = ord(board[i][j])
            if l >= 48 and l <= 57:
                if l in d:
                    return False
                else:
                    d[l] = 1
    d = {}
    for i in range(3,6):
        for j in range(6, 9):
            l = ord(board[i][j])
            if l >= 48 and l <= 57:
                if l in d:
                    return False
                else:
                    d[l] = 1

    d={}
    for i in range(6,9):
        for j in range(0,3):
            l=ord(board[i][j])
            if l >= 48 and l <= 57:
                if l in d:
                    return False
                else:
                    d[l]=1
    d = {}
    for i in range(6,9):
        for j in range(3, 6):
            l = ord(board[i][j])
            if l >= 48 and l <= 57:
                if l in d:
                    return False
                else:
                    d[l] = 1
    d = {}
    for i in range(6,9):
        for j in range(6, 9):
            l = ord(board[i][j])
            if l >= 48 and l <= 57:
                if l in d:
                    return False
                else:
                    d[l] = 1

    return True


