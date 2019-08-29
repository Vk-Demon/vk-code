n=int(input())    # Print the position of first 1 from right to left, in binary representation of an Integer
a,b,c=1,0,0
while(n!=0):
  r=n%2
  a=a*10+r
  n=n//2
lt=[int(i) for i in str(a)]
for i in range(1,len(lt)):
  if(lt[i]==1):
    c=i
    break
print(c)
