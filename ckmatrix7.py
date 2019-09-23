lqz,rc=[input().split(" ") for i in range(5)],0  # Rohan is a coder who loves puzzles involving words and letters. He has recently learnt about the concept of matrices in mathematics and has developed a puzzle in a which a matrix of dimensions 5*5 is filled with letters of the English alphabet. Your task is to help Rohan in displaying the number of rows in which all the 5 vowels in the English alphabet are present.
for i in range(5):
  cv=0
  for j in range(5):
    if(len(lqz[i])==5 and len(set(lqz[i]))==5):
      if(lqz[i][j]=='A' or lqz[i][j]=='a' or lqz[i][j]=='E' or lqz[i][j]=='e' or lqz[i][j]=='I'or lqz[i][j]=='i' or lqz[i][j]=='O' or lqz[i][j]=='o' or lqz[i][j]=='U' or lqz[i][j]=='u'):
        cv=cv+1
  if(cv==5):
    rc=rc+1
print(rc)
