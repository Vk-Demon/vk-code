alp=raw_input()
if((alp >= 'a' and alp <= 'z') or (alp >= 'A' and alp <= 'Z')): 
  if(alp=='a' or alp=='e' or alp=='i' or alp=='o' or alp=='u'):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
