import collections     # Given an array of numbers find the number of occurences of each character and print it in the decreasing order of occurences, if 2 or more numbers occur the same number of times, print the numbers in decreasing order(hint: read about pair STL)
def CountFrequency(a): 
  return collections.Counter(a) 
def frequency(l):
  l1,l2=[],[]
  freq = CountFrequency(l) 
  for k,v in freq.items():
    l1.append(k)
    l2.append(v)
  for i in range(0,len(l2)):                 
    t,t1=l2[i],l1[i]
    j=i-1
    while(t>l2[j] and j>=0):
      l2[j+1]=l2[j]
      l1[j+1]=l1[j]
      j=j-1
    l2[j+1]=t
    l1[j+1]=t1
  if(len(set(l2))==1):
    l1=list(reversed(sorted(l1)))
  else:
    for i in range(0,len(l2)-1):
      if(l2[i]==l2[i+1]):
        if(l1[i]<l1[i+1]):
          t=l1[i]
          l1[i]=l1[i+1]
          l1[i+1]=t
  for i in range(0,len(l1)-1):
    print(l1[i],end=" ")
  print(l1[len(l1)-1],end="")
nnum=int(input())
lt=[int(i) for i in input().split()]
frequency(lt)

'''  INPUT
5
3 3 4 4 7
OUTPUT
4 3 7     '''
