nnum=input()
l=len(nnum)
cb=0
for i in range(0,l):
  if(nnum[i]=="0" or nnum[i]=="1"):
    cb=cb+1
if(cb==l):
  print("yes")
else:
  print("no")
