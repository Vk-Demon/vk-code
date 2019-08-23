n=int(input())             # lexicographically smallest string
lexstr=[]
for i in range(0,n):
  lexstr.append(input())
lexstr=sorted(lexstr)
print(lexstr[0])
