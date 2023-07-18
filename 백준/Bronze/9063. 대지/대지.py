n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
minx=arr[0][0]
maxx=minx
miny=arr[0][1]
maxy=miny

for i in range(1,n):
    if arr[i][0] < minx: minx=arr[i][0]
    elif arr[i][0] > maxx: maxx=arr[i][0]
    if arr[i][1] < miny: miny=arr[i][1]
    elif arr[i][1] > maxy: maxy=arr[i][1]

print(abs(maxx-minx)*abs(maxy-miny))