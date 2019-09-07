nnum=int(input())  # Iron Man wants to extract an infinity stone from a safe. The safe is protected by a password and Iron Man knows the clue to the password which is “sum one and two when sorted they are true”. Decode the clue from the test case and help Iron Man open the safe.
lt=[int(i) for i in input().split()]
ltnum=list(reversed(sorted(lt)))
if(lt==ltnum):
  print(2+1)
