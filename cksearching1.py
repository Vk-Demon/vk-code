nnum=int(input())     #Ria is always fascinated by the number 2. She always wants to know who came second in a race, the second person to set foot on the moon and so on. She is given a list of numbers and asked to find the maximum. As always, she reports the second highest number as the maximum because according to her, 2 is higher than 1. Find out which was the number that Ria would have reported, given a list of N numbers.
slt=[int(i) for i in input().split()]
fmax,smax=max(slt[0],slt[1]),min(slt[0],slt[1])
for i in range(2,nnum):
  if(slt[i]>fmax):
    smax=fmax
    fmax=slt[i]
print(smax)
