num=int(input())
paper=[[0 for _ in range(101)] for _ in range(101)]

for _ in range(num):
    x, y = list(map(int, input().split()))
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j]=1

result=0
for i in paper:
     result+=i.count(1)
print(result)