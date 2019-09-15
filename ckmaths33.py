def expanding(l):     # In a cricket match the coach wanted to check the performance of batsmen o he decided strike rate as criteria. He planned that the two batsmen whose strike rate difference minimum will be sent no. 3 and no.4 in next match.Now your task is to help the coach in finding the two batsmen.
  lx,j=[],1
  for i in range(0,len(l)):
    if(j<len(l)):
      n=(max(l[j],l[i]) - min(l[j],l[i]))
      lx.append(n)
      j=j+1
  for i in range(0,len(lx)):
    if(lx[i]==min(lx)):
      k=i
  print(l[k],l[k+1],sep=" ")
nnum=int(input())
lt=[float(i) for i in input().split()]
expanding(lt)
