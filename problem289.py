#################   With use of extra space of O(m*n)   ##########################
m = len(board)
n = len(board[0])
# print(m, n)
# m=4
# n=3

temp = copy.deepcopy(board)
# print(temp)


for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            c = self.callneighbours(i, j, m, n, board)
            if (c < 2 or c > 3):
                temp[i][j] = 0
        else:  # die cell
            c = self.callneighbours(i, j, m, n, board)
            if (c == 3):
                temp[i][j] = 1
# print(temp)
for i in range(m):
    for j in range(n):
        board[i][j] = temp[i][j]


def callneighbours(self, i, j, m, n, board):
    s = 0
    # print("#########\nFor",i,j)
    if i - 1 >= 0 and j - 1 >= 0:  # upper left
        s += board[i - 1][j - 1]
        # if(board[i-1][j-1])==1:
        #     print("upper left")
    if i - 1 >= 0 and j >= 0:  # upper
        s += board[i - 1][j]
        # if (board[i - 1][j]) == 1:
        #     print("upper")
    if i - 1 >= 0 and j + 1 < n:  # upper right
        s += board[i - 1][j + 1]
        # if (board[i - 1][j + 1]) == 1:
        #     print("upper right")
    if i >= 0 and j - 1 >= 0:  # left
        s += board[i][j - 1]
        # if (board[i][j - 1]) == 1:
        #     print("left")

    if i < m and j + 1 < n:  # right
        s += board[i][j + 1]
        # if (board[i][j + 1]) == 1:
        #     print("right")
    if i + 1 < m and j - 1 >= 0:  # lower left
        s += board[i + 1][j - 1]
        # if (board[i + 1][j - 1]) == 1:
        #     print("lower left")
    if i + 1 < m and j < n:  # lower
        s += board[i + 1][j]
        # if (board[i + 1][j]) == 1:
        #     print("lower")
    if i + 1 < m and j + 1 < n:  # lowerright
        s += board[i + 1][j + 1]
        # if (board[i + 1][j + 1]) == 1:
        #     print("lower right")
    # print(i,j,s)
    return s

#############################   In-place modification   ###############################################3
m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0 or board[i][j] == 2:
                    if self.nnb(board,i,j) == 3:
                        board[i][j] = 2
                else:
                    if self.nnb(board,i,j) < 2 or self.nnb(board,i,j) >3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0

    def nnb(self, board, i, j):
        m,n = len(board), len(board[0])
        count = 0
        if i-1 >= 0 and j-1 >= 0:   count += board[i-1][j-1]%2
        if i-1 >= 0:                count += board[i-1][j]%2
        if i-1 >= 0 and j+1 < n:    count += board[i-1][j+1]%2
        if j-1 >= 0:                count += board[i][j-1]%2
        if j+1 < n:                 count += board[i][j+1]%2
        if i+1 < m and j-1 >= 0:    count += board[i+1][j-1]%2
        if i+1 < m:                 count += board[i+1][j]%2
        if i+1 < m and j+1 < n:     count += board[i+1][j+1]%2
        return count