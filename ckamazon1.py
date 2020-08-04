def miss_num(arr):         # You are given a number n,ranging from 1 to n. Out of which one number is missing. Your task is to print that missing number.
    n = len(arr)
    tot_num = int((n + 1) * (n + 2) / 2)
    s_num = sum(arr)
    return (tot_num-s_num)
nnum=int(input())
lt=[int(i) for i in input().split()]
msng_num = miss_num(lt)
print(msng_num)
