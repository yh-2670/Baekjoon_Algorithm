alpha=input()
word=input()

q=-1
count=1
for i in range(len(word)):
    next=alpha.index(word[i])
    if next<=q:
        q=next
        count+=1
    q=next
print(count)