class Stack:  # Given a string S of length N, find whether the given string is a palindrome using stack or linked list and print 'yes' otherwise print 'no'.
  def __init__(self):
    self.items = []
  def is_empty(self):
    return self.items == []
  def push(self, data):
    self.items.append(data)
  def pop(self):
    return self.items.pop()
s = Stack()
nst=input()
for i in nst:
  s.push(i)
rnst=""
while not s.is_empty():
    rnst = rnst + s.pop()
if(nst == rnst):
    print("yes")
else:
    print("no")

