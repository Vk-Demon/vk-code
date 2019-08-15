isostr=input()
cs,cw=0,0
cs=len(isostr)
cw=len(set(isostr.lower()))
if(cs==cw):
  print("Yes")
else:
  print("No")
