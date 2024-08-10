n=int(input())

for i in range(n):
    print("@"*3*n+" "*n+"@"*n)

for a in range(n*3):
    print("@"*n+" "*n+"@"*n+" "*n+"@"*n)

for p in range(n):
    print("@"*n+" "*n+"@"*3*n)