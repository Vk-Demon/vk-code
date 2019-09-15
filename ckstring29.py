nst,rst=input().split() # Given 2 strings S,X. Print the string after deleting X.If X not found print the same string.
xst=input()
if(xst==nst):
  print(rst)
elif(xst==rst):
  print(nst)
else:
  print(nst,rst,sep=" ")
