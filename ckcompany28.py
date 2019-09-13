nnum=int(input()) # Given a number N and an array of N strings,Print yes, if all strings have atleast one vowel in them otherwise print no.
lt=[input() for i in range(0,nnum)]
tc,c=0,0
for i in lt:
  c=0
  for j in range(0,len(i)):
    if(i[j]=='a' or i[j]=='e' or i[j]=='i' or i[j]=='o' or i[j]=='u'):
      c=1
  tc=tc+c
if(tc==nnum):
  print("yes")
else:
  print("no")
