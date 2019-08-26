def hcf(a,b):   # Shapur has to find weaknesses in the roman army to defeat them.So he gives the army a weakness number.
  if(b==0):     # In Shapur's opinion the weakness of an army is equal to the number of triplets i, j, k such that i < j < k and ai > aj > ak where ax is the power of man standing at position x.
    return a    # The Roman army has one special trait — powers of all the people in it are distinct. Help Shapur find out how weak the romans are.
  else: 
    return hcf(b,a%b)
nnum=int(input())
lt=[int(i) for i in input().split()]
if(lt[1]<lt[0] and lt[2]<lt[1]):
  w=hcf(lt[0],lt[1])
  weak=hcf(w,lt[2])
  print(weak)
else:
  print("0")
