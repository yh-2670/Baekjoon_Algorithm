res=0
q=list(map(int,input().split()))


while True:
    count=0
    res+=1
    for i in range(5):
        if res%q[i]==0:
            count+=1
    if count>=3:
        print(res)
        break