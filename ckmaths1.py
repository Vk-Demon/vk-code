nnum,mnum=input().split()       #Given a number and a number of K, find the greatest number which divides both
nnum,mnum=int(nnum),int(mnum)
k=max(nnum,mnum)
for i in range(1,k+1):
  if(nnum%i==0 and mnum%i==0):
    div=i
print(div)
