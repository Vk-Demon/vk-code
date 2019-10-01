nst=input()  # Given a string, find the length of the longest substring without repeating characters.
sb,lt= [nst[i:j] for i in range(len(nst)) for j in range(i+1, len(nst) + 1)],[]
for i in sb:
  if(len(i)==len(set(i))):
    lt.append(len(set(i)))
print(max(lt))
