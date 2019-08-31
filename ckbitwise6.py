def reverse(bstr):   # Given a binary number convert it to octal
    bstr = "".join(reversed(bstr)) 
    return bstr
bnum=input()
l,l1,l2,l3=['0','4','2','3'],['0','4','2','6','1','5','3','7'],['00','10','01','11'],['000','001','010','011','100','101','110','111']
s,p,c="","",0
ocs=reverse(bnum)
for i in range(0,len(ocs)):
  c=c+1
  s=s+ocs[i]
  if(c==3):
    for j in range(0,len(l3)):
      if(s==l3[j]):
        p=p+l1[j]
    c,s=0,""
if(c==1):
  if(ocs[len(ocs)-1]=='1'):
    p=p+l1[4]
if(c==2):
  for j in range(0,len(l2)):
    if(s==l2[j]):
      p=p+l[j] 
print(reverse(p))
