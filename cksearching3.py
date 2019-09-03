nnum=int(input())  # Ram wants to be a leader. He is fascinated by any puzzle or news that has the word ‘leader’ in it. He comes across a puzzle about finding a leader amongst a list of numbers and is intrigued by the puzzle. As Ram is not good in either maths or logic, he is unable to solve the puzzle. Help Ram by finding out the leader among a given set of positive numbers
ltb=[int(i) for i in input().split()]
leader,c=[],0
for i in range(0,nnum-1):
  c=0
  for j in range(i+1,nnum):
    if(ltb[i]-ltb[j]<0):
      c=c+1
  if(c==0):
    leader.append(ltb[i])
leader.append(ltb[i+1])
for i in leader:
  print(i,end=" ")
