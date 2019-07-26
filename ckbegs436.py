qstr=input()
cn=0
cd=0
cs=0
for i in range(0,len(qstr)):
  if(qstr[i].isnumeric()):
    cn=cn+1
  elif(qstr[i].isalpha()):
    cd=cd+1
  else:
    cs=cs+1
print(cs)
