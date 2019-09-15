def sumofap(a,d,n):  # Given 3 numbers A,B,C find the sum of Arithmetic Series with a=A, d=B and n=C.
  st=0
  i=0
  while(i<n): 
    st=st+a 
    a=a+d 
    i=i+1
  return(st)
anum,dnum,nnum=input().split()
anum,dnum,nnum=int(anum),int(dnum),int(nnum)
print(sumofap(anum,dnum,nnum))
