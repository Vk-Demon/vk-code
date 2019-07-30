xstr,ystr=input().split()
xc,yc=0,0
for i in range(0,len(xstr)):
  xc=xc+1
for j in range(0,len(ystr)):
  yc=yc+1
if(xc>yc):
  print(xstr)
elif(yc>xc):
  print(ystr)
else:
  print(xstr)
