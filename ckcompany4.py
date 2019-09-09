nnum=int(input())  # Given a number N and an array of N elements, find the number of triplets ai < aj < ak(i < j < k) in the array.
lt=[int(i) for i in input().split()]
tri=[]
for i in range(0,len(lt)):
  for j in range(0,len(lt)):
    for k in range(0,len(lt)):
      if(i<j<k and lt[i]<lt[j]<lt[k]):
        tri.append(str(lt[i])+str(lt[j])+str(lt[k]))
print(len(set(tri)))
