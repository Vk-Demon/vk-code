nnum=int(input()) # Given a number N followed by N numbers. All the numbers in the given input appear twice except for one number(ie one number appears only once in the given input). Find the number which appears only once.
ltg=[int(i) for i in input().split()]
for i in range(0,nnum):
  c=0
  for j in range(0,nnum):
    if(ltg[i]==ltg[j]):
      c=c+1
  if(c==1):
    print(ltg[i])
