def imergesort(alist):  # Given an array of size N, find the minimum number of swaps required to sort the array.
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
    return i
nnum=int(input())
ltnum=[int(i) for i in input().split()]
k=imergesort(ltnum)
print(k)
