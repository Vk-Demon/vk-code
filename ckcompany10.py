nst=input()
oc=[]
for i in range(0,len(nst)):
  c=0
  for j in range(0,len(nst)):
    if(nst[i]==nst[j]):
      c=c+1
  oc.append(c)
for i in range(0,len(nst)):
  if(oc[i]!=1):
    print(nst[i].upper(),end="")
  else:
    print(nst[i],end="")
