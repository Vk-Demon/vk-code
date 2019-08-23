oddev=input()                  #swap the even and odd characters
odd,ev="",""
for i in range(0,len(oddev)):
  if(i%2==0):
    ev=ev+oddev[i]
  else:
    odd=odd+oddev[i]
if(len(oddev)%2==0):
  for i in range(0,int(len(oddev)/2)):
    print(odd[i]+ev[i],end="")
else:
  for i in range(0,int(len(oddev)/2)):
    print(odd[i]+ev[i],end="")
  print(ev[i+1],end="")
