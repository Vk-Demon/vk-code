from itertools import permutations  # Given 2 numbers N and K, print the number of ways of taking k elements from the first n elements.
def per(l,n):
  perm = permutations(l,n) 
  c=0
  for i in list(perm): 
    c=c+1
  print(c)
nnum,knum=input().split()
nnum,knum,lt=int(nnum),int(knum),[]
for i in range(1,nnum+1):
  lt.append(i)
per(lt,knum)
