nnum=int(input()) # You are provided with a number ’n’. Your task is to tell whether that number is saturated. A saturated number is a number which is made by exactly two digits.
lt=set(str(nnum))
if(len(lt)==2):
  print("Saturated")
