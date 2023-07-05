arr=[list(map(str, input())) for _ in range(5)]

for i in range(15):
    for j in range(5):
        if len(arr[j])<i+1: continue
        else: print(arr[j][i], end="")