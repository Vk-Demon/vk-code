xnum,opnum,ynum=input().split()
xnum,ynum=int(xnum),int(ynum)
if(opnum=="%"):
  print(xnum%ynum)
else:
  print(int(xnum/ynum))
