def wrtsort(l,f):  # Given an array of N words sort it in ascending order based on the length of the string.If two strings are found to have the same length sort them lexicographically in ascending order.
  for i in range(0,len(l)):                 
    t,t1=f[i],l[i]
    j=i-1
    while(t<f[j] and j>=0):
      f[j+1]=f[j]
      l[j+1]=l[j]
      j=j-1
    f[j+1]=t
    l[j+1]=t1
  return l,f
nnum=int(input())  
lt=[i for i in input().split()]
lt,ft=sorted(lt),[]
for i in range(0,nnum):
  ft.append(len(lt[i]))
wrtsort(lt,ft)
for i in lt:
  print(i,end=" ")
