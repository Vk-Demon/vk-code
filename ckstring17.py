def sbaseword(s1,s2):   # Swagger and Rock are playing a word game. They need to check the two strings use the same base alphabets. Two strings are said to have same base alphabets if the use the same characters to form the word. eg: rescue and curse have same base alphabets - c,e,r,s,u
  if(set(s1)==set(s2)):
    return "true"
  else:
    return "false"
st1,st2=input().split()
print(sbaseword(st1,st2))
