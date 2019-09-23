xo=[input().split(" ",3)for i in range(3)]  # Tron is an expert system which, when given the board configuration and entries, determines the winner of the tic tac toe game. Given a 3*3 tic tac toe board as input, along with the filled in entries, determine which one of the players wins the game. Note: Assume player1 takes X and player2 takes O.
ct,ct1,ct2,ct3,ct4,ct5,ct6,ot,ot1,ot2,ot3,ot4,ot5,ot6=0,0,0,0,0,0,0,0,0,0,0,0,0,0
for i in range(3):
    if(xo[0][i]=="X"):
      ct=ct+1
    elif(xo[0][i]=="O"):
      ot=ot+1
for i in range(3):
    if(xo[i][0]=="X"):
      ct1=ct1+1
    elif(xo[i][0]=="O"):
      ot1=ot1+1
for i in range(3):
    if(xo[i][2]=="X"):
      ct2=ct2+1
    elif(xo[i][2]=="O"):
      ot2=ot2+1
for i in range(3):
    if(xo[i][1]=="X"):
      ct3=ct3+1
    elif(xo[i][1]=="O"):
      ot3=ot3+1
for i in range(3):
    if(xo[2][i]=="X"):
      ct4=ct4+1
    elif(xo[2][i]=="O"):
      ot4=ot4+1
if(xo[0][0]=="X" and xo[1][1]=="X" and xo[2][2]=="X"):
  ct5=ct5+1
if(xo[0][0]=="O" and xo[1][1]=="O" and xo[2][2]=="O"):
  ot5=ot5+1
if(xo[0][2]=="X" and xo[1][1]=="X" and xo[2][0]=="X"):
  ct6=ct6+1
if(xo[0][2]=="O" and xo[1][1]=="O" and xo[2][0]=="O"):
  ct6=ct6+1
if(ct==3 or ct1==3 or ct2==3 or ct3==3 or ct4==3 or ct5==1 or ct6==1):
  print("Player1")  
elif(ot==3 or ot1==3 or ot2==3 or ot3==3 or ot4==3 or ot5==1 or ot6==1):
  print("Player2")  
else:
  print("TIE")
