nnum=int(input())     # Rajesh and Ram are having a conflict on the maximum marks that they have scored in all the exams conducted in the past year. The one having scored the maximum gets a treat from the other. They decide to go through their test papers and record their highest marks. You are Rajesh’s best friend and as he has tutions to attend, he gives you all his test papers and asks you to find out the maximum marks that he has scored among all the marks in all exams. He promises you a treat if he wins the bet with Ram. Help Rajesh find out his highest marks
slt=[int(i) for i in input().split()]
fmax,smax=max(slt[0],slt[1]),min(slt[0],slt[1])
for i in range(2,nnum):
  if(slt[i]>fmax):
    fmax=slt[i]
print(fmax)
