lt=[input() for i in range(6)] # Zaheer is a batsman. He plays a cricket match for six overs and attempts 36 balls. After the match, he analyses his performance and wants to know against which bowler he was able to score the maximum. Help Zaheer find out.
mat =[input().split(" ",6) for x in range (6)]
s,b=0,[]
for i in range(6):
  for j in range(6):
    s=s+int(mat[i][j])
  b.append(s)
  s=0
for i in range(6):
  if(max(b)==b[i]):
    print(lt[i])
