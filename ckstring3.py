nst=input().split()  # Given a string/sentence change it to camelcase.
for i in range(0,len(nst)):
  nst[i]=nst[i].capitalize()
for i in nst:
  print(i,end="")
