rnum,cnum=input().split()  # Lakshmi is in class 12 and is learning about the operations on matrices. Her teacher taught her about the concept of the transpose of a matrix. She is not confident about solving problems based on transpose, and hence decides to practice a lot. She wants to find out if the calculations she has done are correct or not. She asks your help to check whether her answers are correct or if she has made any errors in any of the steps.Write a program to find the transpose of a matrix and help Lakshmi check whether her answers are correct or not.
rnum,cnum=int(rnum),int(cnum)
m=[input().split(" ",cnum)for i in range(rnum)]
l=[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
for i in range(0,cnum):
  print(*l[i],sep=" ")
