arr=[list(map(int, input().split())) for _ in range(9)]
max=0
for i in range(9):
    for j in range(9):
        if arr[i][j]>=max:
            max=arr[i][j]
            n=i+1
            m=j+1
print("{0}\n{1} {2}".format(max, n, m))