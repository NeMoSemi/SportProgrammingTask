#контест на префы

import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())

pref_2 = []
for j in range(n + 2):
    pref = [0] * (m + 2)
    pref_2.append(pref)



for _ in range(q):
    r1, c1, r2, c2, x = map(int, input().split())
    pref_2[r1][c1] += x
    pref_2[r2 + 1][c2 + 1] += x
    pref_2[r1][c2 + 1] -= x
    pref_2[r2 + 1][c1] -= x

for y in range(1, n + 1):
    for x in range(1, m + 1):
        pref_2[y][x] += pref_2[y - 1][x] + pref_2[y][x - 1] - pref_2[y - 1][x - 1]
    print(*pref_2[y][1:-1])
