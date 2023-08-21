import sys
n=int(sys.stdin.readline())
people=list(map(int, sys.stdin.readline().split()))
temp=[]
count=1

while people:
    if people[0]==count:
        people.pop(0)
        count+=1
    else: temp.append(people.pop(0))

    while temp:
        if temp[-1]==count:
            temp.pop()
            count+=1
        else:
            break

if not temp: print("Nice")
else: print("Sad")