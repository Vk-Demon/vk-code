import collections  # Jaspreet is a marketing manager and on inspecting the product ids of products documented as ‘sold’, he finds out that the sales person has repeated a few of the product ids. He decides to warn the sales person who has repeated the same product id thrice. Your task is to find out the number of triplets(ids occurring thrice) of product ids recorded
def CountFrequency(a): 
  return collections.Counter(a) 
def frequency(l):
  l1,l2,tri=[],[],0
  freq = CountFrequency(l) 
  for k,v in freq.items():
    l1.append(k)
    l2.append(v)
  for i in range(0,len(l2)):
    if(l2[i]==3):
      tri=tri+1
  print(tri)
nnum=int(input())
lid=[int(i) for i in input().split()]
frequency(lid)
