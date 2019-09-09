nst=input()  # Given a number N Print the sum of power value for the number of digits given.
npow=len(nst)
sp=0
for i in range(0,npow):
  sp=sp+(int(nst[i])**npow)
print(sp)
