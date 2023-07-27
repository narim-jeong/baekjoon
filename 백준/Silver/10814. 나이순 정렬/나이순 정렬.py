import sys
n=int(sys.stdin.readline())
arr=[list(map(str, sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(arr[i][0], arr[i][1])