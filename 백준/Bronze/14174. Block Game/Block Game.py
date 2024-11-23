howmany=[0]*27

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

n=int(input())
for i in range(n):
    one,two=input().split()
    for j in range(26):
        howmany[j]+=max(one.count(alpha[j]),two.count(alpha[j]))

for i in range(26):
    print(howmany[i])