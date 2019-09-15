nst,kst=input().split()  # Given a string and a number K.Print every kth character from the beginning.
kst,c=int(kst),1
for i in range(0,len(nst)):
  if(c==kst):
    print(nst[i],end=" ")
    c=0
  c=c+1
