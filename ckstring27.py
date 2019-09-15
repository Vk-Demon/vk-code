nst=input() # John cena wants to learn alphabet ordering. He was given a task of ordering of alphabets within a word in a given string. Write a program to help john to order the words.
s,lt="",[]
for i in range(0,len(nst)):
  if(nst[i]!=" "):
    s=s+nst[i]
  else:
    lt.append(''.join(sorted(s)))
    s=""
lt.append(''.join(sorted(s)))
for i in range(0,len(lt)):
  print(lt[i],end=" ")
