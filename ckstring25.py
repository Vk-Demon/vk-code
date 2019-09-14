nst=input().split('.') # You are given with a string which comprises of some numbers. Your task is to find the largest integer present in the string.
nst=str(nst[0])
nst=nst.split(" ")
nt=[]
for i in range(0,len(nst)):
  if(nst[i].isnumeric()):
    nt.append(nst[i])
nt=sorted(nt)
print(nt[len(nt)-1])
