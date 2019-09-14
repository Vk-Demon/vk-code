anum,bnum,cnum=input().split()  # Given 3 angles A,B,C find if they can be interior angles of a triangle.
Input Size : 0 <= A,B,C <= 180
anum,bnum,cnum=int(anum),int(bnum),int(cnum)
if(anum+bnum+cnum==180):
  print("yes")
else:
  print("no")
