import collections   # Given a number N followed by N numbers. Keep the count of each number and print the maximum repeating number.
def CountFrequency(a): 
  return collections.Counter(a) 
def frequency(l):
  a,f=[],[]
  freq = CountFrequency(l) 
  for k,v in freq.items():
    a.append(k)
    f.append(v)
  m=max(f)
  for i in range(0,len(f)):
    if(f[i]==m):
      print(a[i],end=" ")
nnum=int(input())  
ltnum=[int(i) for i in input().split()]
frequency(ltnum)
