import collections  # Given 2 numbers N,K and N arrays each of size K, print the elements that have appeared in all arrays.
def CountFrequency(a): 
  return collections.Counter(a) 
def frequency(l,r):
  l1,l2=[],[]
  freq = CountFrequency(l) 
  for k,v in freq.items():
    l1.append(k)
    l2.append(v)
  for i in range(0,len(l2)):
    if(l2[i]==r):
      print(l1[i],end=" ")
rnum,cnum=input().split()
rnum,cnum=int(rnum),int(cnum)
lt=[int(j) for i in range(rnum) for j in input().split()]
frequency(lt,rnum)
