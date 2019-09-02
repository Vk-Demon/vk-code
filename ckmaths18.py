def fact(n):  # Given 2 numbers N,K print the value of nPk(P-Permutation)
  if(n==0):
    return 1
  else:
    return (n*fact(n - 1))
nnum,knum=input().split()
nnum,knum=int(nnum),int(knum)
p=int((fact(nnum)//(fact(nnum-knum))))
print(p)
