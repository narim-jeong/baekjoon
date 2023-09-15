import sys

def btk():
    if len(arr)==m:
        if sorted(arr)==arr:
            print(*arr)
    else:
        for i in range(1, n+1):
            if i not in arr:
                arr.append(i)
                btk()
                arr.pop()


n, m = map(int, sys.stdin.readline().split())
arr=[]
btk()