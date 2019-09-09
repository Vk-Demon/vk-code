def epselect(lt):  # Given a number N and an array of N elements, a selection algorithm is implemented on this array where numbers at even position would be chosen, the algorithm is again and again implemented on the newly chosen array until only 1 element is remaining. Print the original position(index) of this element in the initial array.
  ep=[]
  for i in range(0,len(lt)):
    if(i%2==1):
      ep.append(lt[i])
  if(len(ep)==1):
    return ep
  else:
    return epselect(ep)
nnum=int(input())
lt=[int(i) for i in input().split()]
ch=epselect(lt)
for i in range(0,nnum):
  if(ch[0]==lt[i]):
    print(i)
