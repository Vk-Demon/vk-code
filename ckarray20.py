def expanding(l):      # You are given an array.Your task is to print the length of longest consecutive subsequence. A longest consecutive subsequence is such that next element differ from previous by 1
  lx,j,c=[],1,1
  for i in range(0,len(l)):
    if(j<len(l)):
      n=(max(l[j],l[i]) - min(l[j],l[i]))
      lx.append(n)
      j=j+1
  for i in range(0,len(lx)):
    if(lx[i]==1):
      c=c+1
  print(c)
nnum=int(input())
lt=[int(i) for i in input().split()]
expanding(sorted(lt))
