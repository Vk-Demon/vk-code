nnum=int(input())  # 
lt,c,bc=[1 for i in range(nnum)],2,0
while(c<=nnum):
  p=c
  for i in range(c,nnum+1):
    if(p<=nnum):
        if(lt[p-1]==0):
          lt[p-1]=1
        else:
          lt[p-1]=0
    p=p+c
  c=c+1
for i in range(0,len(lt)):
  if(lt[i]==1):
    bc=bc+1
print(bc)
'''A man has n buckets. He travels all the bucket and fills the water in bucket which is empty and empty the bucket which is already filled he goes for n times in this manner

On first go 1,2,3,4,5,…n

On second go 2,4,6,8…

On third go 3,6,9…

Your task is to develop a suitable algorithm in order to find the number of buckets which are filled with water at the end of last go.

NOTE: INITIALLY ASSUME EVERY BUCKET IS EMPTY '''
