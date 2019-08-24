def intersection(l1,l2):                   # subset of two list
    l3= [v for v in l1 if v in l2] 
    return l3 
n=int(input())
l1=[int(i) for i in input().split()]
m=int(input())
l2=[int(i) for i in input().split()]
l3=intersection(l1,l2)
c=0
for i in range(0,len(l2)):
  for j in range(0,len(l3)):
    if(l3[j]==l2[i]):
      c=c+1
if(c>0):
  print("Yes")
else:
  print("No")
