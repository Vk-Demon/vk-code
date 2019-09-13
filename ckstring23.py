nstq=input() #Given a string S of length N, print every 3rd character starting from 0th index(print the 0th character also).
if(len(nstq)<3):
  print(nstq[0])
else:
  print(nstq[0]+nstq[3])
