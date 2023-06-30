num=int(input())
for i in range(num):
    for j in range(num-1-i):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print("")
for i in range(num):
    for j in range(i+1):
        print(" ", end="")
    for k in range(2*num-3-2*i):
        print("*", end="")
    print("")