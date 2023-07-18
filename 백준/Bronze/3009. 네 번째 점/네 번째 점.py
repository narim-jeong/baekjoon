arr = [list(map(int, input().split())) for _ in range(3)]

if arr[0][0]==arr[1][0]: print(arr[2][0], end=" ")
elif arr[0][0]==arr[2][0]: print(arr[1][0], end=" ")
else: print(arr[0][0], end=" ")
if arr[0][1]==arr[1][1]: print(arr[2][1])
elif arr[0][1]==arr[2][1]: print(arr[1][1])
else: print(arr[0][1])