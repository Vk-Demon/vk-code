lt=[i for i in input().split()]  # Given a sentence and a string S, find how many times the word occurs
nstr=input()
cw=0
for i in range(0,len(lt)):
  if(nstr==lt[i]):
    cw=cw+1
print(cw)
