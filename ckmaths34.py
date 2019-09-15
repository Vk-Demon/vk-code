nst=input()  # You are given a ‘true’ string. String is called true if weight of string is multiple of 8. Your task is to tell whether a string can be declared True or Not. Weight of string is the sum of ASCII value of Vowel character(s) present in the string.
wt=0
for i in range(0,len(nst)):
  if(nst[i]=='a' or nst[i]=='e' or nst[i]=='i' or nst[i]=='o' or nst[i]=='u'):
    wt=wt+ord(nst[i])
if(wt%8==0):
  print(1)
else:
  print(0)
