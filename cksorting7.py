nnum=int(input()) # Vishal is a competitive coder and he loves problems on sorting and searching. He is bored right now and decides to solve a sorting problem with a modification. He decides to sort the elements at the even indices of an array in ascending order and the elements at the odd indices in descending order. Vishal goes outside his room after coding the solution, but his laptop crashes and he is unable to show it to his teacher. Can you help Vishal by coding the solution to the problem?
lt,at,dt=[int(i) for i in input().split()],[],[]
for i in range(0,nnum):
  if(i%2==0):
    at.append(lt[i])
  else:
    dt.append(lt[i])
at,dt,a,d=sorted(at),list(reversed(sorted(dt))),0,0
for i in range(0,nnum):
  if(i%2==0):
    print(at[a],end=" ")
    a=a+1
  else:
    print(dt[d],end=" ")
    d=d+1

