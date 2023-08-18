import sys
sen=sys.stdin.readline().rstrip()

while sen!='.':
    arr = []
    for i in sen:
        if i == '(' or i == '[': arr.append(i)
        elif i==')':
            if len(arr)>0 and arr[-1]=='(': arr.pop()
            else:
                arr.append(i)
                break
        elif i==']':
            if len(arr)>0 and arr[-1]=='[': arr.pop()
            else:
                arr.append(i)
                break
    if len(arr)==0: print("yes")
    else: print("no")
    sen = sys.stdin.readline().rstrip()