n, m, d, s = map(int, input().split())
milk = [[] for _ in range(n)]
cnt = 0
for i in range(d) :
    person = list(map(int, input().split()))
    milk[person[0] - 1].append(person)

sang = [0] * (m + 1)
for i in range(s) :
    sick = list(map(int, input().split()))
    for j in milk[sick[0] - 1] : 
        if j[2] < sick[1] :
            sang[j[1]] += 1
for i in range(m + 1) :
    if sang[i] < s :
        continue
    med = 0
    for j in milk :
        for k in j :
            if k[1] == i :
                med += 1
                break
    cnt = max(cnt, med)
print(cnt)