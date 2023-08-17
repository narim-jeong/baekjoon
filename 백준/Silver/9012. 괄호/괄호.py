import sys
k=int(sys.stdin.readline())

for _ in range(k):
    arr = []
    testcase=sys.stdin.readline().strip()
    flag=1
    for i in range(len(testcase)):
        if testcase[i]==')':
            if len(arr)==0 or arr[-1]!='(':
                flag=0
                break
            else:
                arr.pop()
        else: arr.append(testcase[i])
    if flag==1 and len(arr)==0: print("YES")
    else: print("NO")