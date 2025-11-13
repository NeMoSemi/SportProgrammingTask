#контест про префы

import sys

input = sys.stdin.readline
def print(x):
    sys.stdout.write(str(x))
    sys.stdout.write('\n')


n, q = map(int, input().split())

s = sorted([int(x) for x in input().split()])
operations = [0] * (n + 1)

for _ in range(q):
    l, r = map(int, input().split())
    operations[l - 1] += 1
    operations[r] -= 1

o = 0
rate = [0] * n
for i in range(n):
    o += operations[i]
    rate[i] = o
rate = sorted(rate)

ans = 0
for i in range(n):
    ans += s[i] * rate[i]

print(ans)
