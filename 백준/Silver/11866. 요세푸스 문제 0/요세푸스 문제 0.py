import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
arr=[x for x in range(1,n+1)]
arr=deque(arr)
print("<", end='')

while True:
    for _ in range(k-1):
        arr.rotate(-1)
    print(arr.popleft(), end='')
    if len(arr)>0: print(", ", end='')
    else:
        print(">")
        break