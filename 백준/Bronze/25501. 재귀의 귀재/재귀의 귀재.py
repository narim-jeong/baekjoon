import sys
def recursion(s, l, r, count):
    if l>=r: return 1, count
    elif s[l]!=s[r]: return 0, count
    else:
        count+=1
        return recursion(s, l+1, r-1, count)

t=int(sys.stdin.readline())
for _ in range(t):
    s=sys.stdin.readline().rstrip()
    count=1
    result, count=recursion(s, 0, len(s)-1, count)
    print(result, count)