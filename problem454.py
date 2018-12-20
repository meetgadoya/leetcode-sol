def fourSumCount(A,B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    res=[]
    c=0
    a=0
    b=0
    c=0
    d=0
    s=0
    A.sort()
    B.sort()
    C.sort()
    D.sort()
    print(A,B,C,D)
    for i in range(len(A)):

        for j in range(len(B)):

            for k in range(len(C)):

                for l in range(len(D)):

                    print("i,j,k,l=",i,j,k,l)
                    if(A[i]+B[j]+C[k]+D[l])==0 and (i, j, k, l) not in res:
                        res.append((i, j, k, l))

                        #print(res)
                        s+=1
                        #print(i, j, k, l)
                        a=i
                        b=j
                        c=k
                        d=l

                        while a<len(A)-1:
                            if a >= 0 and (A[a] == A[a + 1]):
                                s += 1
                                if (a,b,c,d) not in res:
                                    res.append((a, b, c, d))
                                print(a,b,c,d)

                                print("Hey")
                                a+=1
                            else:
                                i=a-1
                                break
                        while b<len(B)-1:
                            if b >= 0 and (B[b] == B[b + 1]):
                                s += 1
                                if (a,b,c,d,) not in res:
                                    res.append((a,b,c,d))


                                print(a,b,c,d)
                                print("HeyB")

                                b+=1
                            else:
                                j=b-1
                                break

                        while c<len(C)-1:
                            if c >= 0 and (C[c] == C[c + 1]):
                                s += 1
                                if (a,b,c,d) not in res:
                                    res.append((a,b,c,d))
                                print(a,b,c,d)
                                print("HeyC")
                                c+=1
                            else:
                                k=c-1
                                break


                        while d<len(D)-1:
                            if d >= 0 and (D[d] == D[d + 1]):
                                s += 1
                                if (a,b,c,d) not in res:
                                    res.append((a,b,c,d))

                                print(a,b,c,d)
                                print("HeyD")

                                d+=1

                            else:
                                l=d-1
                                break

    print(res)
    return len(res)


A=[1,1,-1,-1]
B=[-1,-1,1,1]
C=[1,-1,0,-1]
D=[1,1,-1,1]
print(fourSumCount(A,B,C,D))