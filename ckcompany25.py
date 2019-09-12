nst=input()  # Each character of the alphabet is matched to a number. For example A is mapped to 1 , b to 2 so on z to 26. The reverse mapping is also true. 1 is mapped to a , 2 to b 3 to c and so on z to 26. So a number 12258 can be translated to abbeh , aveh , abyh , lbeh , and lyh , so there are 5 ways to translate 12258. Given a number N , write a program to print the number of ways to do this.
s,c="",0
for i in range(1,len(nst)):
  s=s+nst[i]
  if(int(s)>26):
    c=c+1
  if(len(s)==2):
    s=""
print(len(nst)-c)
