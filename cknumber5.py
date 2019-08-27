ng=input() # whether the number is ‘ajs’ or not.An ‘ajs’ number is a number whose sum of first two digits is present in given number ‘n’
ngk=list(ng)
s,c=0,0
for i in range(0,2):
  s=s+int(ngk[i])
for i in range(0,len(ng)-1):
  if(int(ng[i]+ng[i+1])==s or int(ng[i])==s):
    c=c+1
if(c>0):
  print("1")
else:
  print("0")
