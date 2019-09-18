nnum,nt=int(input()),[]  # First line contains the number of arrays. Subsequent lines contain the size of the array followed by the elements of the array.
for i in range(0,nnum):
  n=int(input())
  lt=[int(i) for i in input().split()]
  lt=sorted(lt)
  for j in range(0,len(lt)):
    nt.append(lt[j])
for i in nt:
  print(i,end=" ")
