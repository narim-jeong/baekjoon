import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
print(*arr, sep='\n')