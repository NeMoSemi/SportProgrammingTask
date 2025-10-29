#спортпрога 29.10.2025

n = int(input())
a = []
for i in range(n):
    x, r, c = map(int, input().split())
    a.append([x, x + r * c])
 
chapalah = 1
for i in range(1, n):
    if a[i][0] > a[i - 1][1]:
        chapalah += 1
print(chapalah)
