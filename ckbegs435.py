qstr=input()
cn=0
for i in range(0,len(qstr)):
  if(qstr[i].isnumeric()):
    cn=cn+1
print(cn)
