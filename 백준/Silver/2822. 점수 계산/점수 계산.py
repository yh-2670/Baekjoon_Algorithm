score=[]
sco=[]
final=[]
finalscore=0

for i in range(8):
    s=int(input())
    score.append(s)
    sco.append(s)

sco.sort()

for i in range(3,8):
    finalscore+=sco[i]
    final.append(score.index(sco[i])+1)

final.sort()
print(finalscore)
print(*final)
