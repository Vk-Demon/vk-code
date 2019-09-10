nnum=int(input())  # Given a number N and array of N integers, print the difference between the indices of smallest and largest number(if there are multiple occurances, consider the first occurance).
lt=[int(i) for i in input().split()]
for i in range(0,nnum):
  if(lt[i]==max(lt)):
    x=i
    break
for i in range(0,nnum):
  if(lt[i]==min(lt)):
    y=i
    break
print(x-y)
