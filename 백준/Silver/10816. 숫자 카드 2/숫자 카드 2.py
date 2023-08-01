import sys
from collections import Counter
n=int(sys.stdin.readline().strip())
arr_n=list(map(int, sys.stdin.readline().strip().split()))
arr_n=Counter(arr_n)
m=int(sys.stdin.readline().strip())
arr_m=list(map(int, sys.stdin.readline().strip().split()))

for i in range(m):
    print(arr_n[arr_m[i]], end=' ')