import sys
import math

n=int(sys.stdin.readline())
tree1=int(sys.stdin.readline())
tree=[]
for i in range(n-1):
    tree2 = int(sys.stdin.readline())
    tree.append(tree2-tree1)
    tree1=tree2

num=tree[0]
for j in range(1,len(tree)):
    num=math.gcd(num, tree[j])

tot=0
for k in range(len(tree)):
    tot+=tree[k]//num-1
print(tot)