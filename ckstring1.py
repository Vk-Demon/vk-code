def rdup(rstr):                    # remove duplicates in string
  unr = ''
  for x in rstr:
    if not(x in unr):
      unr = unr + x
  return unr
rstr=input()
if(len(rstr)%2==1):
  rstr=sorted(rstr)
print(rdup(rstr))
