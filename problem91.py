class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)]
        dp[0] = 1
        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1

        for x in range(2, len(s) + 1):

            if 0 < int(s[x - 1]) <= 9:
                dp[x] += dp[x - 1]
            if 10 <= int(s[x - 2:x]) <= 26:
                dp[x] += dp[x - 2]
        return dp[len(s)]