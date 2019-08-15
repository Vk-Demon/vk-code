nstr=input()
c=0
for i in range(0,len(nstr)):
  if(nstr[i].isnumeric()):
    print(nstr[i],end="")
    c=c+1
if(c==0):
  print()
