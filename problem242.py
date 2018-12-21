def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if(len(s)==len(t)):
        u=[]
        for T in t:
            u.append(T)
        for S in s:
            if S in u:
                u.pop(S)
            else:
                return False
        return True

    else:
        return False
#######################################3    2ND Approach

if (len(s) == len(t)):
    S = list(s)
    T = list(t)
    S.sort()
    T.sort()
    if (S == T):
        return True

return False