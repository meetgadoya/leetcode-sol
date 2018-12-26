def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if(numRows==0):
        return []
    r=[[1]]
    for i in range(2,numRows+1):
        #for j in range(1,i+1):
        s=r[-1]

        #print("S=",s)
        t=[]
        t=callNext(s)
        r.append(t)
        #print(r)
    return r

def callNext(s):
    t=[]
    temp=[0]+s+[0]
    #print(temp,len(s))
    for m in range(1,len(s)+2):
        t.append(temp[m]+temp[m-1])

    #print("T=",t)
    return t


print(generate(5))