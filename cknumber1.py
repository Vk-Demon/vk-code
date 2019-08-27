nnum=int(input())            # you are given with array of numbers.you have to find whether array is beautiful or not. A beautiful array is an array whose sum of all numbers is divisible by 2, 3 and 5
lt=[int(i) for i in input().split()]
s=0
for i in range(0,nnum):
  s=s+lt[i]
if(s%2==0 or s%3==0 or s%5==0):
  print("1")
else:
  print("0")
