import sys
n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
arr_temp=list(set(arr))
arr_temp.sort()
dic={arr_temp[i]:i for i in range(len(arr_temp))}
for j in arr:
    print(dic[j], end=" ")