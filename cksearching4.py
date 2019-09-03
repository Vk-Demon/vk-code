nnum=int(input())  # Prakash is bored and wants to spends his time. He starts rolling a die and observes the value that is shown. He rolls the dice N times and observes that just one number appears distinctly, all the others get repeated or does not appear at all. Find out which was the number that puzzled Prakash for sometime, after which he realised that it was just a coincidence
lt=[int(i) for i in input().split()]
c=0
for i in range(0,nnum):
  c=0
  for j in range(0,nnum):
    if(lt[i]==lt[j]):
      c=c+1
  if(c==1):
    print(lt[i],end=" ")
