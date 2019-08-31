def reverse(bstr):   # Given a binary number convert it to hexadecimal
  bstr = "".join(reversed(bstr)) 
  return bstr
bnum=input()
l,l1,l2,l3=['0','1','2','3'],['0','4','2','6','1','5','3','7'],['00','10','01','11'],['000','001','010','011','100','101','110','111']
l0=['0','8','4','2','1','3','7','F','C','E','A','9','5','D','B','6']
l4=['0000','0001','0010','0100','1000','1100','1110','1111','0011','0111','0101','1001','1010','1011','1101','0110']
s,p,c="","",0
ocs=reverse(bnum)
for i in range(0,len(ocs)):
  c=c+1
  s=s+ocs[i]
  if(c==4):
    for j in range(0,len(l4)):
      if(s==l4[j]):
        p=p+l0[j]
    c,s=0,""
if(c==1):
  if(ocs[len(ocs)-1]=='1'):
    p=p+l1[4]
if(c==2):
  for j in range(0,len(l2)):
    if(s==l2[j]):
      p=p+l[j] 
if(c==3):
  for j in range(0,len(l3)):
    if(s==l3[j]):
      p=p+l1[j]
print(reverse(p))
