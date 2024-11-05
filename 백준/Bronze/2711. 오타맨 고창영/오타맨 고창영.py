n=int(input())

for i in range(n):
    new=''
    miss,word=input().split()
    for j in range(len(word)):
        if j==int(miss)-1:
            continue
        else:
            new+=word[j]
    print(new)