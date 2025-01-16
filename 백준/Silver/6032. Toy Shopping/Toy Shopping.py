alll=[]
hs=[]


n=int(input())

for i in range(n):
    j,p=map(int,input().split())
    alll.append([j/p,j,p,i])

alll.sort(reverse=True)

P=0
a=[]

for i in range(3):
    P+=alll[i][2]
    a.append(alll[i][3]+1)

print(P)

for i in range(3):
    print(a[i])