n=int(input())

for i in range(n):
    moos=input()
    if 'MOO' in moos:
        print(len(moos)-3)
    elif 'OOO' in moos or 'MOM' in moos:
        print(len(moos)-2)
    elif 'OOM' in moos:
        print(len(moos)-1)
    else:
        print(-1)