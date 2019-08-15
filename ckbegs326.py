def imergesort(alist):
  if len(alist)>1:
    mid = len(alist)//2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]
    imergesort(lefthalf)
    imergesort(righthalf)
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
      if lefthalf[i] < righthalf[j]:
        alist[k]=lefthalf[i]
        i=i+1
      else:
        alist[k]=righthalf[j]
        j=j+1
      k=k+1
    while i < len(lefthalf):
      alist[k]=lefthalf[i]
      i=i+1
      k=k+1
    while j < len(righthalf):
      alist[k]=righthalf[j]
      j=j+1
      k=k+1
nnum=int(input())
xlist=[int(i) for i in input().split()]
imergesort(xlist)
for i in xlist:
  print(i,end=" ")
