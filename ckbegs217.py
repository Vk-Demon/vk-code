xnum=int(input()) 
tmp=xnum 
tsum=0      
while tmp>0:
  rem=tmp%10  
  tsum=tsum+rem**3  
  tmp/=10   
if(xnum==tsum):  
  print("yes")  
else:  
  print("no")  
