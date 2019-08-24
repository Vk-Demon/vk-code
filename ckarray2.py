n,k=input().split()           # Given 2 numbers N,K and an array of N strings, find if any K consecutive strings are same
n,k,l=int(n),int(k),[]
for i in range(0,n):
  l.append(input())
l=set(l)
t=len(l)-1
if(k==(n-t)):
  print("yes")
else:
  print("no")
