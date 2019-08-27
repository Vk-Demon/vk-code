n,k=input().split() # Find ground of a number (defined as the number which is just smaller or equal to the number k given to you)
n,k=int(n),int(k)
lt=[int(i) for i in input().split()]
lt2=[]
for i in range(0,n):
  if(k-lt[i]>0):
    lt2.append(k-lt[i]) 
  else:
    lt2.append(k+1)
for i in range(0,n):
  if(lt2[i]==min(lt2)):
    gnd=i
print(lt[gnd])
