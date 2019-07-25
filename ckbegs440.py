n=int(input())
def fibo(n):
  if(n<=1):
    return n
  else:
    return(fibo(n-1)+fibo(n-2))
for i in range(1,n+1):
  print(fibo(i),end=" ")
