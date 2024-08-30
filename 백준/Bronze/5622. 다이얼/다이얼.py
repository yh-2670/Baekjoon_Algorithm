n=input()
q=0
dial=['ABC','DEF','GHI','GKL','MNO','PQRS','TUV','WXYZ']
a=[2,3,4,5,6,7,8,9]

for i in n:
    for j in range(len(dial)):
        if i in dial[j]:
            q+=a[j]+1
print(q)