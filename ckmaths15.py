import collections   # Shreya is a brilliant girl. She likes to memorize the numbers. These numbers will be shown to her. As an examiner develop an algorithm to test her memory
def CountFrequency(a): 
  return collections.Counter(a) 
def frequency(l,m):
  l1,l2,l3,c=[],[],[],0
  freq = CountFrequency(l) 
  for k,v in freq.items():
    l1.append(k)
    l2.append(v)
  for i in range(0,len(m)):
    for j in range(0,len(l1)):
      if(m[i]==l1[j]):
        l3.append(l2[j])
        c=1
    if(c==0):
      l3.append("Not Present")
    c=0   
  return(l3)
nnum=int(input())
nlt=[int(i) for i in input().split()]
knum=int(input())
mlt=[int(i) for i in input().split()]
lt=frequency(nlt,mlt)
for i in lt:
  print(i,end=" ")
