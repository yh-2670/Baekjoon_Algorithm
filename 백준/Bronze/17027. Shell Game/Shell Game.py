n = int(input())
A = []
B = []
C = []
for i in range(n) :
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
S = []
for i in range(3) :
    p =[0, 0, 0]
    p[i] = 10
    score = 0
    for j in range(n) :
        p[A[j] - 1], p[B[j] - 1] = p[B[j] - 1], p[A[j] - 1]
        if p[C[j] - 1] == 10 :
            score += 1
    S.append(score)
print(max(S))