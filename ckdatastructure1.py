def fact(n):   # Given 2 numbers A,B. print the value of a!/b!.
  if(n==0):
    return 1
  else:
    return (n*fact(n-1))
anum,bnum=input().split()
anum,bnum=int(anum),int(bnum)
print(int(fact(anum)//fact(bnum)))
