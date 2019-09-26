import collections   # Given 2 numbers N,K and an array of N elements, print the number(s) that has been repeated K times.Print them in ascending order if there are more than one number to be printed.If no element satisfies the pattern then print -1.
def CountFrequency(a): 
  return collections.Counter(a) 
def frequency(l,kn):
  l1,l2,tl,c=[],[],[],0
  freq = CountFrequency(l) 
  for k,v in freq.items():
    l1.append(k)
    l2.append(v)
  for i in range(len(l2)):
    if(l2[i]==kn):
      tl.append(l1[i])
      c=c+1
  if(c>0):
    print(*tl,sep=" ")
  else:
    print(-1)
nnum,knum=input().split()
nnum,knum=int(nnum),int(knum)
lt=[int(i) for i in input().split()]
frequency(lt,knum)
