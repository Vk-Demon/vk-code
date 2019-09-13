nnum=int(input())  # There is one meeting room in Flipkart. There are n meetings in the form of (S [ i ], F [ i ]) where S [ i ] is start time of meeting i and F [ i ] is finish time of meeting i Given a number N followed by 2 arrays S and F of sizes N and N, What is the maximum number of meetings that can be accommodated in the meeting room assuming the room can only accommodate one meeting at a time.
slt=[int(i) for i in input().split()]
flt=[int(i) for i in input().split()]
cn,ft=0,0
if(flt[0]<slt[1]):
  ft=flt[0]
  cn=cn+1
for i in range(1,nnum):
  if(ft<slt[i]):
    ft=flt[i]
    cn=cn+1
print(cn)
