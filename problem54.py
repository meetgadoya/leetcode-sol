# my solution
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def helper(i_st, i_end, j_st, j_end):
            lis = []
            i = i_st
            j = j_st
            while(j <= j_end):
                lis.append(matrix[i][j])
                self.v[i][j] = 1
                j = j + 1
            i = i + 1
            j = j - 1
            while(i <= i_end):
                lis.append(matrix[i][j])
                self.v[i][j] = 1
                i = i + 1
            j = j - 1
            i = i -1
            while(j >= j_st):
                lis.append(matrix[i][j])          
                self.v[i][j] = 1
                j = j - 1
            i = i - 1
            j = j + 1
            while(i > i_st):
                lis.append(matrix[i][j])
                self.v[i][j] = 1
                i = i -1

            return lis
        m = len(matrix) # no of row
        if m == 0:
            return []
        n = len(matrix[0]) # no of columns
        res = []
        if m == 1:
            return matrix[0]
        if n == 1:
            for i in range(len(matrix)):
                res.append(matrix[i][0])
            return res
        
        self.v = [[0 for a in range(n)] for b in range(m)]
        i_st = 0 
        j_st = 0
        i_end = m-1
        j_end = n-1
        while(i_st < i_end and j_st < j_end):
            res += helper(i_st, i_end, j_st, j_end)
            i_st += 1
            j_st += 1
            i_end -= 1
            j_end -= 1
        
        # for sqaure matrix
        if m==n and i_st == i_end and j_st == j_end:
            res.append(matrix[i_st][j_st])
            return res
        
        # for cases where one side is been covered.
        if j_st < j_end:
            for j in range(j_st, j_end+1):
                if self.v[i_st][j] == 0:
                    res.append(matrix[i_st][j])
        if i_st < i_end:
            for i in range(i_st, i_end+1):
                if self.v[i][j_st] == 0:
                    res.append(matrix[i][j_st])
        
        return res
        
        
# other more optimal and easy solution
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
