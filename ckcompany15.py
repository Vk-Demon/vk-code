nnum=int(input())  # Given N strings and a prefix string p. Find how many of the N strings have p as their prefix. for eg: String[] input={'100','111','10100','10','1111'} prefix='10' output=2. 
lt=[i for i in input().split()]
pfx=input()
cp=0
for i in range(0,len(lt)):
  s,st=lt[i],""
  for i in range(0,len(s)):
    st=st+s[i]
    if(st==pfx):
      cp=cp+1
print(cp)
