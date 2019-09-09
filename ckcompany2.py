nnum=int(input()) # Given a number n followed by n numbers. Find the numbers which are equal to their index value and print them in sorted order. If no such numbers are present print '-1' without quotes.
lt=[int(i) for i in input().split()]
qt,cn=[],0
for i in range(0,nnum):
  if(lt[i]==i):
    qt.append(lt[i])
    cn=1
if(cn>0):
  for i in qt:
    print(i,end=" ")
else:
  print(-1)
