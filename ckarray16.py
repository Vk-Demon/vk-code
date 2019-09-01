nnum=int(input())      # You are given an array of ids of prisoners. The jail authority found that there are some prisoners of same id. Your task is to help the authority in finding the common ids
lt=[int(i) for i in input().split()]
st=[]
for i in range(0,len(lt)-1):
  if(lt[i]==lt[i+1]):
  	print(lt[i],end="")
