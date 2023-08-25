import sys
from collections import deque

n=int(sys.stdin.readline())
arr=deque(enumerate(map(int, sys.stdin.readline().split())))

for _ in range(n):
    idx, paper = arr.popleft()
    print(idx+1, end=' ')
    if paper>0: arr.rotate(-(paper-1))
    else: arr.rotate(-paper)