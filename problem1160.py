class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        for word in words:
            char_list = list(chars)
            flag = True
            for each_char_word in word:
                if each_char_word in char_list:
                    char_list.remove(each_char_word)
                else:
                    flag = False
                    break
            if flag == True:
                res += len(word)
        return res
########################################################################################################################
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        count = {}
        for c in chars:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        ans = 0
        for w in words:
            copy = dict(count)
            y = True
            for c in w:
                if c not in copy or copy[c] == 0:
                    y = False
                    break
                else:
                    copy[c] -= 1
            if y:
                ans += len(w)
        return ans

########################################################################################################################
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0

        org = {}
        for char in chars:
            if char in org:
                org[char] += 1
            else:
                org[char] = 1

        for word in words:
            if len(word) > len(chars):
                continue
            flag = True
            org_copy = dict(org)
            for each_char_word in word:
                if each_char_word not in org_copy or org_copy[each_char_word] == 0:
                    flag = False
                    break
                else:
                    org_copy[each_char_word] -= 1

            if flag == True:
                res += len(word)
        return res