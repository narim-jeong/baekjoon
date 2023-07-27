import sys
n=int(sys.stdin.readline())
arr=[str(sys.stdin.readline()) for _ in range(n)]
arr_temp=list(set(arr))
arr_temp.sort()
arr_temp.sort(key=lambda x: len(x))
print(*arr_temp, sep='')