p1,p2=input().split()  # Check whether the given 4 points form a square or not.
q1,q2=input().split()
r1,r2=input().split()
s1,s2=input().split()
p1,p2,q1,q2,r1,r2,s1,s2=int(p1),int(p2),int(q1),int(q2),int(r1),int(r2),int(s1),int(s2)
d12=(p1-q1)*(p1-q1)+(p2-q2)*(p2-q2)
d13=(p1-r1)*(p1-r1)+(p2-r2)*(p2-r2)
d14=(p1-s1)*(p1-s1)+(p2-s2)*(p2-s2)
d23=(q1-r1)*(q1-r1)+(q2-r2)*(q2-r2)
d24=(q1-s1)*(q1-s1)+(q2-s2)*(q2-s2)
d32=(r1-q1)*(r1-q1)+(r2-q2)*(r2-q2)
d34=(r1-s1)*(r1-s1)+(r2-s2)*(r2-s2)
if (d12==d13 and 2 * d12==d14 and 2*d24==d23):
  c=1 
elif (d13==d14 and 2*d13==d12 and 2*d32==d34): 
  c=1
elif (d12==d14 and 2*d12==d13 and 2*d23==d24):
  c=1
else:
  c=0
if(c==1):
  print("yes")
else:
  print("no")
