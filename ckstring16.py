nrstr=input()              # Given a sentence S of 2 words reverse the order of two words
nrstr=nrstr.split(" ")
nrstr=nrstr[-1::-1]
rstr= ' '.join(nrstr)
print(rstr)
