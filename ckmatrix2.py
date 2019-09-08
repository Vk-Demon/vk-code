xo=[input().split(" ",3)for i in range(3)]  # Tron is an expert system which, when given the board configuration and entries, determines the winner of the tic tac toe game. Given a 3*3 tic tac toe board as input, along with the filled in entries, determine which one of the players wins the game. Note: Assume player1 takes X and player2 takes O.
ct,ct1,ct2,ct3,ct4,ct5,ct6=0,0,0,0,0,0,0
for i in range(3):
    if(xo[0][i]=="X"):
      ct=ct+1
for i in range(3):
    if(xo[i][0]=="X"):
      ct1=ct1+1
for i in range(3):
    if(xo[i][2]=="X"):
      ct2=ct2+1
for i in range(3):
    if(xo[i][1]=="X"):
      ct3=ct3+1
for i in range(3):
    if(xo[2][i]=="X"):
      ct4=ct4+1
if(xo[0][0]=="X" and xo[1][1]=="X" and xo[2][2]=="X"):
  ct5=ct5+1
if(xo[0][2]=="X" and xo[1][1]=="X" and xo[2][0]=="X"):
  ct6=ct6+1
if(ct==3 or ct1==3 or ct2==3 or ct3==3 or ct4==3 or ct5==1 or ct6==1):
  print("Player1")  
else:
  print("Player2")
