'''
Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation:
You throw one die with 6 faces.  There is only one way to get a sum of 3.

Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation:
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation:
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation:
You throw one die with 2 faces.  There is no way to get a sum of 3.

Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation:
The answer must be returned modulo 10^9 + 7.

'''


# slow but easy solution
def numRollsToTarget(self, d, f, target):
    """
    :type d: int
    :type f: int
    :type target: int
    :rtype: int
    """

    l = [1 for i in range(d)]

    res = set()
    i = -1
    flag = 0
    while l[0] <= f:
        if sum(l) == target:
            res.add(tuple(l))
        i = -1
        #logic: always increment last bit by 1 and check whether it has increased over f or not
        l[i] += 1

        if l[i] > f:

            while l[i] > f:
                l[i] = 1
                i = i - 1
                if abs(i) <= len(l):
                    l[i] += 1
                else:
                    flag = 1
                    break

        # print(l)
        if flag == 1:
            break
    return len(res) % (10 ** 9 + 7)

########################################################################################################################
class Solution(object):
    # def find_all_permut(self,)

    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        memo = {}

        def solve(d, target):
            if d == 0:
                if target > 0:
                    return 0
                return 1
            if (d, target) in memo:
                return memo[(d, target)]
            res = 0
            for k in range(max(0, target - f), target):
                res += solve(d - 1, k)
            memo[(d, target)] = res
            return memo[(d, target)]

        return solve(d, target) % (10 ** 9 + 7)


########################################################################################################################
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for i in range(target + 1)] for j in range(d + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                k = 1
                while k <= min(j, f):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % mod
                    k += 1
        return dp[d][target] % mod



########################################################################################################################
class Solution(object):
    # def find_all_permut(self,)

    def numRollsToTarget(self, d, f, target):

        if target < d * 1 or target > f * d:
            return 0

        m = [[0] * (target + 1) for row in range(d + 1)]

        for i in range(1, min(f, target) + 1):
            m[1][i] = 1

        for i in range(2, d + 1):
            for j in range(i, min(target, f * i) + 1):
                for k in range(max(1, j - f), j):
                    m[i][j] = (m[i][j] + m[i - 1][k]) % 1000000007

        return m[d][target]