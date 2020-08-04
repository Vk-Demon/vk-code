nnum,knum=input().split()       # Given 2 numbers N and K and followed by an array of N integers. The given element K is removed from the array and new array is printed. If after removing every occurance of K the array becomes empty, print 'empty' without quotes.
nnum,knum=int(nnum),int(knum)
lt=[int(i) for i in input().split()]
slt,c=[],0
for i in lt:
    if(knum != i):
       slt.append(i)
       c+=1
if(c>0):
    print(*slt,sep=" ")
else:
    print("empty")
