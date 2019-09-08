encds=input()  # Given a string of length N, print the encoded string by adding 3 to each character(x maps to a,y maps to b,z maps to c).
ec=[]
for i in range(0,len(encds)):
  ec.append(ord(encds[i])+3)
for j in range(0,len(ec)):
  if(ec[j]<91):
    print(chr(ec[j]),end="")
  elif(ec[j]==91):
    print("A",end="")
  elif(ec[j]==92):
    print("B",end="")
  elif(ec[j]==93):
    print("C",end="")
