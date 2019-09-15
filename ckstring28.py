fnst=input()  # you are given with two strings.Your task is to check whether one of the string is substring of the other.If substring exists,then print the starting index of sub-string.
lnst=input()
fst,lst,c=max(fnst,lnst),min(fnst,lnst),-1
for i in range(0,len(fst)):
  s=fst[i]
  for j in range(i+1,len(fst)):
    s=s+fst[j]
    if(s==lst):
      c=i+1   
print(c)
