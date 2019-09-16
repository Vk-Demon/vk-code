nnum=int(input())  # Varsha is a Machine learning scientist. She wants to apply a few ML algorithms on the dataset to do some research and for that, she wants to merge two given arrays and sort them in ascending order. You are an intern working under Varsha and she has asked for your help for the same. Given 2 arrays arr1[] and arr2[], find the union of both the arrays sorted in ascending order.  Note: Union of two arrays must have distinct elements.
nt=[int(i) for i in input().split()]
mnum=int(input())
mt=[int(i) for i in input().split()]
lt=sorted(set((mt+nt)))
for i in lt:
  print(i,end=" ")
