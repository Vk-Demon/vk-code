def accordian(l):  # Given an array N, check if the values are alternating between increasing and decreasing
  j=1
  lx=[]
  for i in range(0,len(l)):
    if(j<len(l)):
      n=(max(l[j],l[i]) - min(l[j],l[i]))
      lx.append(n)
      j=j+1
  cx,cy=0,0
  j=1
  for i in range(0,len(lx)):
    if(j<len(lx)):
      if(lx[i]<lx[j]):
          cx=cx+1
      elif(lx[i]==lx[j]):
          cy=cy+1
      else:
          cx=cx-1
    j=j+1
  if(cx>0 or cy>0):
    return "no"
  else:
    return "yes"
nnum=int(input())
lt=[int(i) for i in input().split()]
print(accordian(lt))
