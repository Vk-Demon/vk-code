nst=input()  # You are given a string ‘s’.Your task is to print the string in the order they are present and then sum of digits.
st=0
for i in range(0,len(nst)):
  if(nst[i].isnumeric()):
    st=st+int(nst[i])
  else:
    print(nst[i],end="")
print(st)
