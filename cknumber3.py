def cmp(lt,cnum,k):    # the smallest positive natural number which is not present  in given list and in addition to it,the number should not be equal to the sum of any combination of ‘n’ numbers present in the list.You have to develop a suitable algorithm in order to find that number ‘m’
  c=0
  lt=sorted(lt)
  for i in range(0,cnum-1):
    for j in range(i+1,cnum):
      if (lt[i]+k==lt[j]):
        c=k
  if(c==0):
    return k
  else:
    return 0
cnum=int(input())
lt=[int(i) for i in input().split()]
g=0
for i in range(1,cnum):
  cp=cmp(lt,cnum,i)
  n=i
  if(cp>0):
    g=cp
    break
print(g)
