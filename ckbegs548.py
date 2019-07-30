nz=int(input())
z=0
ary=[int(i) for i in input().split()]
for i in range(0,len(ary)):
  z=z+ary[i]
z=int(z/nz)
for i in range(0,len(ary)):
  if(z==i):
    print(z)
