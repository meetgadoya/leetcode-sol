########################        MAXIMAL SQUARE      ##########################
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if (len(matrix) == 0 or len(matrix[0]) == 0):
            return 0

        if (len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0][0] == '1'):
            return 1
        dp = [0] * (len(matrix[0]) + 1)
        h = len(matrix)
        w = len(matrix[0])

        prev = 0
        maxlen = 0
        # print(dp)
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                temp = dp[j]
                if (matrix[i - 1][j - 1] == '1'):
                    dp[j] = min(min(prev, dp[j - 1]), dp[j]) + 1
                    maxlen = max(maxlen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
                # print(dp)
        return maxlen * maxlen
