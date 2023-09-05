import sys
from collections import Counter

n=int(sys.stdin.readline())
arr=sorted([int(sys.stdin.readline()) for _ in range(n)])

print(round(sum(arr)/n))
print(arr[n//2])

if n==1: print(arr[0])
else:
    count_list=sorted(Counter(arr).items(), key=lambda x: (-x[1], x[0]))
    if count_list[0][1] != count_list[1][1]: print(count_list[0][0])
    else: print(count_list[1][0])

print(max(arr)-min(arr))


