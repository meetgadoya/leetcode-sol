class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        m = len(board)
        n = len(board[0])

        stack = []
        m_lis = [0, m - 1]
        n_lis = [0, n - 1]
        for i in m_lis:
            for j in range(n):
                if board[i][j] == "O":

                    stack.append((i, j))
                    while len(stack) > 0:
                        a, b = stack.pop(0)
                        if board[a][b] == "O":
                            board[a][b] = "Y"
                            if b + 1 < n and board[a][b + 1] == "O":
                                stack.append((a, b + 1))
                            if a + 1 < m and board[a + 1][b] == "O":
                                stack.append((a + 1, b))
                            if b > 0 and board[a][b - 1] == "O":
                                stack.append((a, b - 1))
                            if a > 0 and board[a - 1][b] == "O":
                                stack.append((a - 1, b))
        for i in range(m):
            for j in n_lis:
                if board[i][j] == "O":
                    # convert_all(board,0i,m,n)
                    # board[i][j]= "Y"
                    stack.append((i, j))
                    while len(stack) > 0:
                        a, b = stack.pop(0)
                        if board[a][b] == "O":
                            board[a][b] = "Y"
                            if b + 1 < n and board[a][b + 1] == "O":
                                stack.append((a, b + 1))
                            if a + 1 < m and board[a + 1][b] == "O":
                                stack.append((a + 1, b))
                            if b > 0 and board[a][b - 1] == "O":
                                stack.append((a, b - 1))
                            if a > 0 and board[a - 1][b] == "O":
                                stack.append((a - 1, b))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"