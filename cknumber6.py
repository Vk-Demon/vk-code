import collections   # You are given an array of digits. Your task is to print the digit with maximum frequency
def CountFrequency(a): 
  return collections.Counter(a) 
n=int(input())
a=[int(i) for i in input().split()]
l1,l2=[],[]
freq = CountFrequency(a) 
for k,v in freq.items():
  l1.append(k)
  l2.append(v)
for i in range(0,len(l2)):
  if(l2[i]==max(l2)):
    g=i
print(l1[g])
