def stair(s):  # There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Given a number N Count the number of ways, the person can reach the top.
  way=[1,2]
  if(s<=len(way)):
    return way[s-1]
  else:
    nw=stair(s-1)+stair(s-2)
    way.append(nw)
    return nw
nnum=int(input())
print(stair(nnum))
