import sys
n=int(sys.stdin.readline())
arr_n=set(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
arr_m=list(map(int, sys.stdin.readline().split()))

for i in arr_m:
    if i in arr_n: print(1, end=' ')
    else: print(0, end=' ')