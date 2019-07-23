nnum=int(input())
ary=[int(i) for i in input().split()]
arysort=sorted(ary)
for i in range(0,nnum):
  print(arysort[i],end=" ")
