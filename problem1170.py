'''
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.



Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").

'''
# logic my good soln runtime: 88ms beats 76%
import bisect
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        # if len(queries) == 0 :
        # count = 0
        # for word
        final_res_q = [0 for each in queries]
        for i, each_q_word in enumerate(queries):
            if len(each_q_word) == 0:
                final_res_q[i] = 0
                continue
            temp = [0 for _ in range(26)]
            min_char = 26
            for char in each_q_word:
                char_val = ord(char) - ord('a')
                if char_val < min_char:
                    min_char = char_val
                temp[char_val] += 1
            final_res_q[i] = temp[min_char]

        final_res_w = [0 for each in words]
        for i, each_w_word in enumerate(words):
            if len(each_w_word) == 0:
                final_res_w[i] = 0
                continue
            temp = [0 for _ in range(26)]
            min_char = 26
            for char in each_w_word:
                char_val = ord(char) - ord('a')
                if char_val < min_char:
                    min_char = char_val
                temp[char_val] += 1
            final_res_w[i] = temp[min_char]

        final_res = []

        final_res_w.sort()
        # print(final_res_q)
        for i, each_q_word in enumerate(final_res_q):
            idx = bisect.bisect_left(final_res_w, each_q_word + 1)
            # print(idx)

            final_res.append(len(final_res_w) - idx)
        return final_res




# logic : more shorter version , runtime = 52 ms beats 98%
import bisect


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        query_lis = [each_query.count(min(each_query)) for each_query in queries]
        word_lis = sorted([word.count(min(word)) for word in words])

        res = []
        for q in query_lis:
            res.append((len(word_lis) - bisect.bisect(word_lis, q)))
        return res




