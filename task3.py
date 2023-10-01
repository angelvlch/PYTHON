import random

M = 4
A = [ [0]*M for i in range(M) ]
for i in range(M):
    for j in range(M):
        # m=(random.randint(0, 10))
        # A[i][j]=m
        A[i][j]=A[j][i]=(random.randint(0,10))# для симметричной матрицы

print(A)

for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        if A[i][j]!=A[j][i]:
            print("Матрица не симметричная!")
            exit()
print("Матрица симметричная")