nnum=int(input())  # You are given some pens of specific serial number whenever a new pen is inserted you have to print the new arrangement of pens in sorted order. 
nt=[int(i) for i in input().split()]
mnum=int(input())
mt=[int(i) for i in input().split()]
for i in range(0,len(nt)):
  mt.append(nt[i])
  mt=sorted(mt)
  print(*mt,sep=" ")
