pwnum=input()      # Given a number N, Print sum of power of the given integer(Assumption : the input is 12345 and the output is output=(1^0)+(2^1)+(3^2)+(4^3)+(5^4)).
sb=0
for i in range(0,len(pwnum)):
  sb=sb+(int(pwnum[i])**i)
print(sb)
