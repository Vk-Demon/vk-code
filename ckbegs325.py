nnum=int(input())
ary=[int(i) for i in input().split()]
arysort=sorted(ary)
median=int((nnum+1)/2)
print(arysort[median-1])
