lt=[i for i in input().split()]  # Given a sentence interchange the words around the word 'and'.
for i in range(0,len(lt)):
  if(lt[i]=='and'):
    t=lt[i-1]
    lt[i-1]=lt[i+1]
    lt[i+1]=t
for i in lt:
  print(i,end=" ")
