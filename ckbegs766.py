primenum=int(input())
cpx=0
for i in range(1,primenum+1):
  if(primenum%i==0):
    cpx=cpx+1
if(cpx==2):
  print("yes")
else:
  print("no") 
