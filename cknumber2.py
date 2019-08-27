inum=int(input()) # You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique
lt=[int(i) for i in input().split()]
for i in range(0,inum):
  if(lt[i]==max(lt)):
    l=i
  elif(lt[i]==min(lt)):
    s=i
print(l-s)
