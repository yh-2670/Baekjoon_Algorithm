n=int(input())

m=input()

rep=[]
for i in range(n):
    for j in range(n):
        cnt=0
        for k in range(i+1,n):
            if m[i:i+j]==m[k:k+j]:
                cnt+=1
            if cnt==1:
                rep.append(j+1)
print(max(rep))