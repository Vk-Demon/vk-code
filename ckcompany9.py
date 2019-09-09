nnum=int(input())  # Given 2 arrays check if they are mirror images of each other.Input Size : N <= 1000000.
lt=[int(i) for i in input().split()]
mlt=[int(i) for i in input().split()]
if(lt==list(reversed(mlt))):
  print("yes")
else:
  print("no")
