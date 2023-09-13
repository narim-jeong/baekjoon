import sys

def recur(N):
    if N==1: return ['*']
    star=recur(N//3)
    arr=[]

    for i in star: arr.append(i*3)
    for j in star: arr.append(j+' '*(N//3)+j)
    for k in star: arr.append(k * 3)

    return arr


N =int(sys.stdin.readline())
print('\n'.join(recur(N)))