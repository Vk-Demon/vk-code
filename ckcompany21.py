nst,k=input().split()   # Given a string and a number K, change every kth character to uppercase from beginning in string.
k=int(k)
c=k
for i in range(len(nst)):
  if(i==c-1):
    print(nst[i].upper(),end="")
    c+=k
  else:
    print(nst[i],end="")
