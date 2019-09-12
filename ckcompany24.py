nnum,dnum=input().split() # Print the position of first 1 from left to right, in binary representation of product of 2 integers after the first one.
nnum,dnum=int(nnum),int(dnum)
nnum=nnum*dnum
a,b,c,kt,nxt=1,0,0,[],0
while(nnum!=0):
  r=nnum%2
  a=a*10+r
  nnum=nnum//2 
while(a!=0):
  r=a%10
  b=b*10+r
  a=a//10
b=str(int(b/10))
for i in range(len(b)):
  if(b[i]=='1'):
    c=c+1
    if(c==2):
      nxt=i+1
print(nxt)
