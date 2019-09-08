astr,bstr=input().split()  # Given 2 strings check whether they differ by only one character.Input Size : |s| <= 100000(complexity O(nlogn) or O(n))
astr,bstr=list(set(astr)),list(set(bstr))
if(len(astr)==len(bstr)):
  print("yes")
else:
  print("no")
