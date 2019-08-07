tstr=input()
ct,cs=0,0
for i in range(0,len(tstr)):
  if(tstr[i].isalnum()):
    ct=ct+1
  if(tstr[i].isspace()):
    cs=cs+1
if(cs==0 and ct>0):
  print("Yes")
else:
  print("No")
  
