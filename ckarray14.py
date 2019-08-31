knum=int(input())   # Find the count k by which array has been rotated in the rotated sorted array. Given a number N followed 2 arrays A and B of length N. Find the amount K by which the array has been rotated
lt=[int(i) for i in input().split()]
lt2=[int(i) for i in input().split()]
c1,c2=0,0
for i in range(0,len(lt2)):
  if(lt2[i]==knum):
    c1=i+1
for i in range(0,len(lt)):
  if(lt[i]==knum):
    c2=i+1
c3=(len(lt)-c1)+c2
print(c3)
