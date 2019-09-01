nnum=int(input())  # Given a number N and an array of N integers, find the sum of the sums obtained by considering all consecutive pairs of adjacent elements
lt=[int(i) for i in input().split()]
tsum=0
for i in range(0,nnum-1):
    tsum=tsum+lt[i]+lt[i+1]
print(tsum)
