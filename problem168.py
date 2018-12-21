def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    d=[x-64 for x in range(ord('A'),ord('Z')+1)]
    print(d)
    c=0
    i=0
    for a in reversed(s):
        m=ord(a)-65 #ASCII
        if c==0:
            c+=d[m]
            i=i+1
        else:
            c+=d[m]*pow(26,i)
            i=i+1
        #c+=(d[ord(a)-65]+1)+i*26
        #print(c)
        #i=i+1
        print(c)
    return c

