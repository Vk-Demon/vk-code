n=int(input())                       # find the minimum distance between the elements in the array
l=[int(i) for i in input().split()]
ek,en=input().split()
ek,en,c,e=int(ek),int(en),0,0
for i in range(0,len(l)):
  if(l[i]==ek):
    c=i
  elif(l[i]==en):
    e=i
print(max(c,e)-min(c,e))
