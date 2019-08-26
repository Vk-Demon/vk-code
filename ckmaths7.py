anum,bnum,cnum=input().split()           # Given 3 numbers A,B,C find if they can form the sides of a triangle
anum,bnum,cnum=int(anum),int(bnum),int(cnum)
a,b,c=anum*anum,bnum*bnum,cnum*cnum
if(a+b==c):
  print("yes")
else:
  print("no")
