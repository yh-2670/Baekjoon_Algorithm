t = int(input())

for i in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    res = 0
    a = max(num)
    b = sum(num)
    c = max(a, 1)
    
    for j in range(c, b + 1) :
            if b % j == 0 :
                summ = 0
                for k in range(len(num)) : 
                    summ += num[k]
                    if summ > j : 
                        break
                    elif summ == j:
                        summ = 0

                else :
                    res = n - b // j
                    break
    print(res)