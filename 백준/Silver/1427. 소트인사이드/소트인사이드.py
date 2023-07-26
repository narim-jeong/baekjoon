n=int(input())
arr=list(map(int, str(n)))
arr.sort(reverse=True)
print(*arr, sep='')