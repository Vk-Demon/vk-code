def coprime(x,y):                  # co-prime
  if(y==0):
    return x
  else:
    return coprime(y,x%y)
fstr,lstr=input().split()
f,l=len(fstr),len(lstr)
c=coprime(f,l)
if(c==1):
  print("yes")
else:
  print("no")
