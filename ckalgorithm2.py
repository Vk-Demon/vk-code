an1,an2=input().split()  # Given 3 points check whether they can lie on the same line.
bn1,bn2=input().split()
cn1,cn2=input().split()
an1,an2,bn1,bn2,cn1,cn2=int(an1),int(an2),int(bn1),int(bn2),int(cn1),int(cn2)
cdist=int((an1*(bn2-cn2)+bn1*(cn2-an2)+cn1*(an2-bn2))/2)
if(cdist==0):
  print("yes")
else:
  print("no")
