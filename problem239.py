#########################################           WORKS FOR SNALLER CASES(TIME LIMIT EXCEEDS)          ####################################3
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """

    # res=helper(s,wordDict,0)
    word=s
    # while(len (word)>0):
    i=1
    while(i<= len(word)):
        print(word[:i],i)
        if(word[:i] in wordDict):
            res=helper(word[i:],wordDict)
            if(res==True):
                return True
        i=i+1
        # if (len(word) == 0):
        #     return True
        # if (word not in wordDict and i >= len(word) or i >= len(prev)):
        #     return False
    return res


def helper(word,wordDict):
    res=False
    i = 1
    if(len(word)==0):
        res=True
    while (i <= len(word)):
        print(word[:i], i)
        if (word[:i] in wordDict):
            res = helper(word[i:], wordDict)
        i = i + 1
    return res



##########################################################################################################################3
def wordBreak( s, wordDict):


    f = [False] * (len(s) + 1)
    f[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            print(s[j:i])
            if (f[j] and s[j:i] in wordDict):
                f[i] = True
                break
    return f[len(s)];
####################################            ALMOST CORRECT          ################################################
# print(wordBreak("leetcode",["leet","code"]))
