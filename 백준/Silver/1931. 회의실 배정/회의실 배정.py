time=[]

n=int(input())

for i in range(n):
    t=list(map(int,input().split()))
    time.append(t)

time.sort(key=lambda x: (x[1],x[0]))

end = time[0][1]

count=1

for i in range(1,n):
    if end<=time[i][0]:
        count+=1
        end=time[i][1]

print(count)