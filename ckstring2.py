sgstr=input()  # Given a string S, find if the strings 'Vishal' and 'Sundar' is present in the string.
s,c="",0
for i in range(0,len(sgstr)):
  if not(sgstr[i].isalpha()):
    s=""
  elif(sgstr[i].isalpha()):
    s=s+sgstr[i]
    if(s=="Vishal" or s=="Sundar"):
      c=c+1
if(c==2):
  print("yes")
else:
  print("no")
