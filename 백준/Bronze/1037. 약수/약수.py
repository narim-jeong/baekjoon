import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
if len(arr)==1: print(arr[0]**2)
else: print(min(arr)*max(arr))