sstr=input()
mda=int(len(sstr)/2)
mdb=mda-1
if(len(sstr)%2==0):
  for i in range(0,len(sstr)):
    if(i==mdb or i==mda):
      print("*",end="")
    else:
      print(sstr[i],end="")  
else:
  for i in range(0,len(sstr)):
    if(i==mda):
      print("*",end="")
    else:
      print(sstr[i],end="") 
