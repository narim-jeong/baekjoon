import sys
from collections import deque
n=int(sys.stdin.readline())
arr=[x for x in range(1,n+1)]
arr=deque(arr)

while len(arr)>1:
    arr.popleft()
    arr.append(arr.popleft())
print(*arr)