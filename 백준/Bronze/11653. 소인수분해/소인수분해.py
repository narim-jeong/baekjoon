N = int(input())
if N==1: exit()
while True:
    for i in range(2,N+1):
        if N%i==0:
            print(i)
            if i==N: exit()
            N=N//i
            break