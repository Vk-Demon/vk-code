anum,bnum,cnum=input().split()    # Given 3 numbers A,B,C find if they can form the sides of a scalene triangle
anum,bnum,cnum=int(anum),int(bnum),int(cnum)
if not(anum==bnum or bnum==cnum or cnum==anum):
  print("yes")
else:
  print("no")
