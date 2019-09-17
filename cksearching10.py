def intersection(l1,l2):  # Bala is the CEO of a company and decides to reward a few hardworking employees with an extra bonus.  He wants to find out the number of employees who are working parallely on two different projects and give them a bonus. The ids of employees working on a particular project are stored in an array.Given two arrays project1 and project2, find out whether the employees working on project2 are a subset of employees working on project1.
    l3= [v for v in l1 if v in l2] 
    return l3 
n=int(input())
l1=[int(i) for i in input().split()]
m=int(input())
l2=[int(i) for i in input().split()]
l3=intersection(l1,l2)
c=0
for i in range(0,len(l2)):
  for j in range(0,len(l3)):
    if(l3[j]==l2[i]):
      c=c+1
if(c<len(l2)):
  print("No")
else:
  print("Yes")
