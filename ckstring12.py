sstr=input()                             # vowels ascending
vstr,cstr,kstr="","",""
l=[]
for i in range(0,len(sstr)):
  if(sstr[i]=="a" or (sstr[i]=="e") or (sstr[i]=="i") or (sstr[i]=="o") or (sstr[i]=="u")):
    vstr=vstr+sstr[i]
    l.append(i)
  else:
    cstr=cstr+sstr[i]
vstr=sorted(vstr)
if(len(l)>1):
  k,n=0,0
  for i in range(0,len(sstr)):
    if(k<len(l)):
      if(i==l[k]):
        print(vstr[k],end="")
        k=k+1
      else:
        print(cstr[n],end="")
        n=n+1
    else:
        print(sstr[i],end="")  
elif(len(l)==1):
  for i in vstr:
    print(i,end="")
  print(cstr)
else:
  print(sstr)
