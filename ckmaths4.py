nnum=input()                  # Given a number N, print the product of digits
s=1 
for i in range(0,len(nnum)):
   s=s*int(nnum[i])
print(s)
