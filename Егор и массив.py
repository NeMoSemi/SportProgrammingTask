#контест про префы

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [int(x) for x in input().split()]

operations = []
for _ in range(m):
    l, r, d = map(int, input().split())
    operations.append([l, r, d])

operations_list = [0] * (m + 2)
for _ in range(k):
    l, r = map(int, input().split())
    operations_list[l - 1] += 1
    operations_list[r] -= 1

for i in range(1, m):
    operations_list[i] += operations_list[i - 1]


pref = [0] * (n + 2)
for i in range(m):
    delta = operations_list[i] * operations[i][2]
    pref[operations[i][0] - 1] += delta
    pref[operations[i][1]] -= delta

o = 0
for i in range(n):
    o += pref[i]
    a[i] += o

print(*a)
