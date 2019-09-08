ascstr=input() # Given a string S convert each of the characters into numbers(ASCII) and print the sum of the numbers.
sc=0
for i in range(0,len(ascstr)):
  sc=sc+ord(ascstr[i])
print(sc)
