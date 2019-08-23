pstr,qstr=input().split()               # generate password
p,q=len(pstr),len(qstr)
k=1
if(p<q):
  for i in range(0,p):
    print(pstr[i]+qstr[i],end="")
  for j in range(p,q):
    print(k,qstr[j],end="",sep="")
    k=k+1
if(p>q):
  for i in range(0,q):
    print(pstr[i]+qstr[i],end="")
  for j in range(q,p):
    print(k,pstr[j],end="",sep="")
    k=k+1
if(p==q):
  for i in range(0,q):
    print(pstr[i]+qstr[i],end="")
