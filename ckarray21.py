stnum=input()  # A number is given as input. Find the maximum number that can be formed using the digits
ft=list(reversed(sorted(stnum)))
for i in ft:
  print(i,end="")
