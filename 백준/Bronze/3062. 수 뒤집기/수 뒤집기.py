n=int(input())
for i in range(n):
    m=input()
    a=m[::-1]
    q=int(a)+int(m)
    w=str(q)[::-1]
    if str(q)==w:
        print("YES")
    else:
        print("NO")