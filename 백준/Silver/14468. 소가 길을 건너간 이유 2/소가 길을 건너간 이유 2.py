cow=input()
cnt=0

for i in range(52):
    for j in range(i+1,52):
        if cow[i] == cow[j]:
            crop = cow[i + 1 : j]
            for o in range(len(crop)):
                if crop.count(crop[o])==1:
                    cnt+=0.5
print(int(cnt))