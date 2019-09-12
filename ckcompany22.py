nnum,knum=input().split()  # Given two numbers N,K(N>=K) and an array of N elements, write a program to find the Kth largest element.
nnum,knum=int(nnum),int(knum)
lt=[int(i) for i in input().split()]
lt=list(reversed(sorted(lt)))
print(lt[knum-1])
