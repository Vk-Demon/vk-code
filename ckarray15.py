def expanding(l):      # Given an array, find the minimum difference between any two elements in that array
  lx,j=[],1
  for i in range(0,len(l)):
    if(j<len(l)):
      n=(max(l[j],l[i]) - min(l[j],l[i]))
      lx.append(n)
      j=j+1
  print(min(lx))
nnum=int(input())
lt=[int(i) for i in input().split()]
expanding(lt)
