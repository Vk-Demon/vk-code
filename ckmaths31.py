def fact(n):  # Rohan’s teacher wants to teach him about permuting the numbers.He is given an assignment,in which he is given a number,His task is to print the sum of all permutations that can be made up using those digits.
  if(n==0):
    return 1
  else:
    return (n*fact(n-1))
nnum=int(input())
lsb,m,c=0,nnum,0
while(m>0):
  r=m%10
  lsb=lsb+r
  m=m//10
  c=c+1
lsb=lsb*int(fact(c)/c)
st,s=10**(c-1),lsb
while(st>1):
  s=s+(lsb*st)
  st=st//10
print(s)
