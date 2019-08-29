
#logic : runtime = 72ms beats 65%
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []

        def helper(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):
                if self.pal(s[:i]):
                    helper(s[i:], path + [s[:i]], res)

        helper(s, [], res)
        return res

    def pal(self, s):
        return s == s[::-1]