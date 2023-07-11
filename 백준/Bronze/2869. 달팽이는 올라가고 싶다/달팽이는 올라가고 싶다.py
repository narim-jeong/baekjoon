import math

A, B, V = map(int, input().split())
print(int(math.ceil((V-B)/(A-B))))