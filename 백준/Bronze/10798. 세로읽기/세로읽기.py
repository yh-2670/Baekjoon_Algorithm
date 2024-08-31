w=[input() for i in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(w[j]):
            print(w[j][i], end='')