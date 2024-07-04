n=int(input())

for i in range(n):
      m=int(input())
      P1=0
      P2=0
      for j in range(m):
          a,b=input().split()
          if a=='P' and b=='R' or a=='R' and b=='S' or a=='S' and b=='P':
              P1=P1+1
          if a=='R' and b=='P' or a=='S' and b=='R' or a=='P' and b=='S':
              P2=P2+1
      if P1>P2:
          print("Player 1")
      elif P2>P1:
          print ("Player 2")
      else:
          print("TIE")