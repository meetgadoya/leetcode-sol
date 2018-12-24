A = [[1] * m] * n
# print A

for j in range(1, n):
    for i in range(1, m):
        # print(j,i)
        A[j][i] = A[j][i - 1] + A[j - 1][i]
# print(A)
return (A[n - 1][m - 1])

