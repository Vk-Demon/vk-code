from itertools import permutations  # Given a number N, find the smallest number which is greater than N with the same digits in N. If N is the greatest digit print 'impossible'.
def per(l,st):
  nt=[]
  perm = permutations(l) 
  for i in list(perm): 
    s=''
    for j in range(0,len(i)):
      s=s+str(i[j])
    if(s!=st and int(s)>int(st)):
      nt.append(int(s))
  return(nt)
nst=input()
lt=[int(nst[i]) for i in range(0,len(nst))]
nt=per(lt,nst)
if(len(nt)==0):
  print("impossible")
else:
  print(min(nt))
    
