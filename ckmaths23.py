nrnum=input()  # Given a number N, check whether it has repeating digits.
if(len(nrnum)==len(set(nrnum))):
  print("no")
else:
  print("yes")
