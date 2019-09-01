onum=int(input())  # An organization named “Gupil” has a well-maintained library in its own building. Librarian orders and gets books for the library very frequently. Each book which is newly arrived has its own unique serial number. The books initially are placed in descending order. The librarian want to place a new book without disturbing the descending order of books in terms of unique id. Now you must help librarian to find the right spot for placing the book
old=[int(i) for i in input().split()]
nnum=int(input())
new=[int(i) for i in input().split()]
newspot,c,d=[],0,3,
for i in range(0,c+len(new)):
  for j in range(0,len(old)-1):
    if(new[i]>old[0]):
      newspot.append(j+1)
      old.append(new[i])
      old=list(reversed(sorted(old)))
      c=c+1
    if(old[j]>new[i] and new[i]>old[j+1]):
      newspot.append(j+2)
      old.append(new[i])
      old=list(reversed(sorted(old)))
      c=c+1
    if(j==len(old)-2):
      if(new[i]<old[j+1]):
        newspot.append(j+d)
        d=d+1
for i in range(0,len(newspot)-1):
  print(newspot[i],end=" ")
print(newspot[len(newspot)-1],end="")
