dstr,k=input().split()          # Given a number N and a number K, check if it has all digits from 0 to k in it
k,c=int(k),0
for i in range(0,len(dstr)):
  for j in range(0,k+1):
    if(int(dstr[i])==j):
      c=c+1 
if(c>k):
  print("yes")
else:
  print("no")
