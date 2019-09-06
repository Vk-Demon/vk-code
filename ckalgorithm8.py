nnum=int(input())   # Given a number N, followed by an array of N elements, check if it is sorted.
lt=[int(i) for i in input().split()]
ltnum=sorted(lt)
if(lt==ltnum):
  print("yes")
else:
  print("no")
