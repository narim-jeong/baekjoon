num = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))

for i in range(6):
    print(num[i]-found[i], end="")
    if i < 6: print(" ", end="")