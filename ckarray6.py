def reverse(n):         # Given a number N, check if the sum of the digits is a Palindrome. Print YES or NO
  r=0
  while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
  return r
k=input()
s=0
for i in range(0,len(k)):
  s=s+int(k[i])
rs=reverse(s)
if(s==rs):
  print("YES")
else:
  print("NO")
