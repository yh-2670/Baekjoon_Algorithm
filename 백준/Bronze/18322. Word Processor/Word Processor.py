n,k=map(int,input().split())

words=list(input().split())

final=[]

wordcount=0
for i in range(n):
    if len(words[i])+wordcount>k:
        print(*final)
        final=[]
        wordcount=0

    wordcount+=len(words[i])
    final.append(words[i])

print(*final)