import collections   # Given a number N followed by N numbers. Out of these N numbers some of them are repeated. Write a program to find the first number which is repeated. If no numbers are repeated print 'unique'.
def CountFrequency(a): 
  return collections.Counter(a) 
def frequency(l):
  l1,l2,c=[],[],0
  freq = CountFrequency(l) 
  for k,v in freq.items():
    l1.append(k)
    l2.append(v)
  for i in range(0,len(l2)):
    if(l2[i]>1):
      c=1
      print(l1[i],end="")
      break
  if(c==0):
    print("unique")
nnum=int(input())
lt=[int(i) for i in input().split()]
frequency(lt)
