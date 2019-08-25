def leftrotate(a, d, n):   # left rorate array after k operation
  for i in range(gcd(d,n)):  
    t = a[i] 
    j = i 
    while 1: 
      k = j + d 
      if k >= n: 
        k = k - n 
      if k == i: 
        break
      a[j] = a[k] 
      j = k 
    a[j] = t   
def array(arr, size): 
  for i in range(size): 
    print("%d" % arr[i], end=" ") 
def gcd(a, b): 
  if b == 0: 
    return a; 
  else: 
    return gcd(b, a%b) 
n,k=input().split()
n,k=int(n),int(k)
lt=[int(i) for i in input().split()]
leftrotate(lt,k,n) 
array(lt,n)
