x,y=input().split()
p,q=input().split()
x,y=int(x),int(y)
p,q=int(p),int(q)
m=max(x,p)
n=min(x,p)
a=max(y,q)
b=min(y,q)
print(m-n,a-b)