q=[["Algorithm",204],["DataAnalysis",207],["ArtificialIntelligence",302],["CyberSecurity",'B101'],["Network",303],["Startup",501],["TestStrategy",105]]

n=int(input())
for i in range(n):
    a=input()
    for j in range(7):
        if a == q[j][0]:
            print(q[j][1])