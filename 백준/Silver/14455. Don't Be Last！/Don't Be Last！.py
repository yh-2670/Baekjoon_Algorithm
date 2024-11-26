dic = {}
n=1000
k = 0

for i in range(int(input())):
    a, b = input().split()
    b = int(b)
    if a not in dic.keys():
        dic[a] = b
    else:
        dic[a] += b
        
name = list(dic.keys())

if len(dic.keys()) == 7:
    for i in (list(dic.values())):
        if min(dic.values()) < i < n:
            n = i
else:
    n= min(dic.values())

for i in (list(dic.values())):
    if i == n:
        k += 1

if k != 1:
    print("Tie")
    
elif len(dic.keys()) == 7:
    for i in range(len((list(dic.values())))):
        if (list(dic.values()))[i] == n:
            print(name[i])
            
else:
    for i in range(len((list(dic.values())))):
        if (list(dic.values()))[i] == min(dic.values()):
            print(name[i])