bowl,lt=[input().split(" ",3)for i in range(5)],[]  # Jasprit Bumrah’s bowling is being analysed by the Indian coach. The pitch is modelled as a rectangular matrix and the point at which the ball bounces is recorded. A ball which leads to a wicket is marked with a ‘W’ at the place it bounces. The coach wants to know the place at which the ball bounced, which led to the maximum number of wickets. The points at which the ball didn’t lead to a wicket are marked with a ‘B’.
for i in range(5):
  c=0
  for j in range(3):
    if(bowl[i][j]=="W"):
      c=c+1
  lt.append(c)
for i in range(0,len(lt)):
  if(lt[i]==max(lt)):
    print(i+1)
