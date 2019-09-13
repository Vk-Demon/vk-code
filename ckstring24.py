nst=input() # Given a string change upper case to lower case and lower case to upper case.
for i in range(0,len(nst)):
  if(nst[i].isupper()):
    print(nst[i].lower(),end="")
  else:
    print(nst[i].upper(),end="")
