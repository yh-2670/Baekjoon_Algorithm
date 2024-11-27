n = int(input())
cows = []

for i in range(n):
    arrive, time = map(int, input().split())
    cows.append((arrive, time))

cows.sort()

current = 0

for arrive, time in cows:
    current = max(current, arrive) + time

print(current)
