import sys
import math
a_upper, a_lower = map(int, sys.stdin.readline().split())
b_upper, b_lower = map(int, sys.stdin.readline().split())
lower=math.lcm(a_lower, b_lower)
upper=a_upper*(lower//a_lower) + b_upper*(lower//b_lower)
div=math.gcd(lower, upper)
print(upper//div, lower//div)