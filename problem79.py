class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        h = len(board)
        w = len(board[0])
        v = [[False] * w for _ in range(h)]
        flag = False
        for i in range(h):
            for j in range(w):
                if (board[i][j] == word[0]):
                    flag = self.helper(board, i, j, h, w, word, v)
                    if (flag == True):
                        return True

        return flag

    def helper(self, board, i, j, h, w, word, v):
        # global flag
        if (len(word) == 0):
            # flag=True
            return True
        if (-1 < i < h and -1 < j < w):

            if (board[i][j] == word[0] and v[i][j] == False):
                v[i][j] = True
                res = self.helper(board, i + 1, j, h, w, word[1:], v) or self.helper(board, i - 1, j, h, w, word[1:],v) or self.helper(board, i, j + 1,h, w, word[1:],v) or self.helper(board, i, j - 1, h, w, word[1:], v)
                v[i][j] = False
                return res

            else:
                return False
        else:
            return False

