def binary(lt,k):  # Given 2 numbers N,K followed by a sorted array of N elements, search and tell if an element K is present.(Do it in logN time complexity)
	beg=0
	end=len(lt)-1
	found=0
	while(beg<=end and not found):
		mid=(beg+end)//2
		if(lt[mid]==k):
			found=1
		else:
			if(k<lt[mid]):
				end=mid-1
			else:
				beg=mid+1	
	return found
nnum,knum=input().split()
nnum,knum=int(nnum),int(knum)
ltnum=[int(i) for i in input().split()]
f=binary(ltnum,knum)
if(f==1):
  print("Yes")
else:
  print("No")
