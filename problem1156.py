'''
Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.

Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.

Example 3:

Input: text = "aaabbaaa"
Output: 4

Example 4:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.

Example 5:

Input: text = "abcdef"
Output: 1

'''

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        if len(text) == 0:
            return 0
        li = []
        li.append((text[0], 1))
        for i in range(1, len(text)):
            if li[-1][0] == text[i]:
                char, freq = li.pop()
                li.append((char, freq + 1))
            else:
                li.append((text[i], 1))
        # print(li)
        d = {}
        for i in range(len(text)):
            if text[i] in d:
                d[text[i]] += 1
            else:
                d[text[i]] = 1
        # print(d)
        # created both the required structures

        # case 1: just extend a particular group by 1
        res = max(min(freq + 1, d[char]) for char, freq in li)

        # case 2: merge 2 different groups
        for i in range(1, len(li) - 1):
            if li[i - 1][0] == li[i + 1][0] and li[i][1] == 1:
                res = max(res, min(li[i - 1][1] + li[i + 1][1] + 1, d[li[i + 1][0]]))
                # print(res, li[i-1][1] + li[i-1][1] + 1)
        return res