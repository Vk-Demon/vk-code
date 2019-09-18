def min_sum(l):  # Quinton was given an array of integers and was asked to find the minimum subarray sum. A subarray is a contiguous non-empty segment of an array.
  sb,mt=[l[i:j] for i in range(len(l)+1) for j in range(i+1,len(l)+1)],[]
  for i in sb:
    s=0
    for j in range(len(i)):
      s=s+i[j]
    mt.append(s)
  print(min(mt))
nnum=int(input())
lt=[int(i) for i in input().split()]
min_sum(lt)
