nnum,mnum=input().split()
nnum,mnum=int(nnum),int(mnum)
def rgcd(nnum,mnum):
  if(mnum==0):
    return nnum
  else:
    return rgcd(mnum,nnum%mnum)
print(rgcd(nnum,mnum))
