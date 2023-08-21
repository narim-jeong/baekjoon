import sys
n=int(sys.stdin.readline())
arr=[]
i=0

for _ in range(n):
    sent=sys.stdin.readline().strip()
    if sent=='pop':
        if len(arr)-i==0: print(-1)
        else:
            print(arr[i])
            i+=1
    elif sent=='size': print(len(arr)-i)
    elif sent=='empty':
        if len(arr)-i==0: print(1)
        else: print(0)
    elif sent=='front':
        if len(arr)-i==0: print(-1)
        else: print(arr[i])
    elif sent=='back':
        if len(arr)-i==0: print(-1)
        else: print(arr[-1])
    else:
        arr.append(sent[5:])