n=int(input())
list=[int(i) for i in input().split()]
s,k=0,0
for i in list:
  for j in range(k,n):
    s=s+list[j]
  print(s,end=" ")
  s=0
  k=k+1
