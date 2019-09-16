def binary(nnum):  # Ram loves bit magic. He is given a set of integers, and wants to sort them based on the number of 1s in their binary representations ( in descending order). Help Ram do a little bit of bit magic!
  a,b=1,0
  while(nnum!=0):
    r=nnum%2
    a=a*10+r
    nnum=nnum//2 
  while(a!=0):
    r=a%10
    if not(r==0):
      b=b*10+r
    a=a//10
  b=str(int(b/10))
  return b
n=int(input())
lt,xt=[int(i) for i in input().split()],[]
for i in range(0,n):
  xt.append(binary(lt[i]))
for i in range(0,len(lt)):                 
  t,t1=xt[i],lt[i]
  j=i-1
  while(t>xt[j] and j>=0):
    xt[j+1]=xt[j]
    lt[j+1]=lt[j]
    j=j-1
  xt[j+1]=t
  lt[j+1]=t1
for i in lt:
  print(i,end=" ")
