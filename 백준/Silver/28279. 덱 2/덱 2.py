import sys
from collections import deque

n=int(sys.stdin.readline())
arr=[]
arr=deque(arr)

for _ in range(n):
    sent=sys.stdin.readline().split()

    if sent[0]=='1': arr.appendleft(sent[1])
    elif sent[0]=='2': arr.append(sent[1])
    elif sent[0]=='3':
        if len(arr)==0: print(-1)
        else: print(arr.popleft())
    elif sent[0]=='4':
        if len(arr)==0: print(-1)
        else: print(arr.pop())
    elif sent[0]=='5':
        print(len(arr))
    elif sent[0]=='6':
        if len(arr)==0: print(1)
        else: print(0)
    elif sent[0]=='7':
        if len(arr)==0: print(-1)
        else: print(arr[0])
    elif sent[0]=='8':
        if len(arr)==0: print(-1)
        else: print(arr[-1])