import sys
from collections import deque

n=int(sys.stdin.readline())
type=sys.stdin.readline().split()
arr_num=sys.stdin.readline().split()
m=int(sys.stdin.readline())
num=sys.stdin.readline().split()

queuestack=deque()

for i in range(n):
    if type[i]=='0': queuestack.append(arr_num[i])
if len(queuestack)==0:
    print(*num, end=" ")
    exit()

for j in range(m):
    queuestack.appendleft(num[j])
    print(queuestack.pop(), end=" ")