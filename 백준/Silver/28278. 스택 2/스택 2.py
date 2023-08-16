import sys

n=int(sys.stdin.readline())
stack=[]
for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if len(command)>1:
        stack.append(int(command[2:]))
    elif command=='2':
        if len(stack)==0: print(-1)
        else:
            print(stack.pop())
    elif command=='3': print(len(stack))
    elif command=='4':
        if len(stack)==0: print(1)
        else: print(0)
    else:
        if len(stack)==0: print(-1)
        else: print(stack[-1])