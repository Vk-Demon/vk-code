vstr=input()
cv=0
for i in range(0,len(vstr)):
  if(vstr[i]=="a" or vstr[i]=="e" or vstr[i]=="i" or vstr[i]=="o" or vstr[i]=="u" or vstr[i]=="A" or vstr[i]=="E" or vstr[i]=="I" or vstr[i]=="O" or vstr[i]=="U"):
    cv=cv+1
if(cv>0):
  print("yes")
else:
  print("no")
