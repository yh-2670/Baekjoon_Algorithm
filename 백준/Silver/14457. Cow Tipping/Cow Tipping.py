alll=[]
n=int(input())

for i in range(n):
    a=list(map(int,input()))
    alll.append(a)

count=0
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if alll[i][j] == 1:
            count+=1
            for x in range(i+1):
                for y in range(j+1):
                    if alll[x][y] == 1:
                        alll[x][y] = 0
                    else:
                        alll[x][y] = 1
print(count)