while True:
    a,b,c = list(input().split())
    b=int(b)
    c=int(c)
    if a=='#' and b==0 and c==0:
        break
    elif b>17 or c>=80:
        print(a,'Senior')
    else:
        print(a,'Junior')