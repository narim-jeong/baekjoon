import sys
n=int(sys.stdin.readline())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
arr_x=sorted(arr, key=lambda x : (x[1], x[0]))
for a, b in arr_x:
    print(a, b)