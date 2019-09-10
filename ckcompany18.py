def divide(n1,n2):    # Divide two given integers A and B without using multiplication, division and mod operator. If it is overflow, return MAX_INT.
  if (n1 == 0): return 0
  if (n2 == 0): return INT_MAX   
  ngr = 0 
  if (n1 < 0): 
    n1 = - n1 
    if (n2 < 0): 
      n2= -n2  
    else: 
      ngr = True 
  elif (n2 < 0): 
    n2= -n2  
    ngr = True  
  quo = 0
  while (n1 >= n2): 
    n1= n1-n2  
    quo+=1
  if (ngr): 
    quo = - quo  
  return quo
anum,bnum=input().split()
anum,bnum=int(anum),int(bnum)
print(divide(anum,bnum))
