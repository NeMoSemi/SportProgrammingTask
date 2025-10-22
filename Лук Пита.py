#контест по спортпроге 22 октябся(условия не копируются)
import sys
 
 
try:
    sys.stdin = open('bow.in')
    sys.stdout = open('bow.out', 'w')
except:
    pass
 
n = int(input())
 
if n == 1:
    a, b = map(int, input().split())
    print(a + b)
 
else:
    x, d = map(int, input().split())
    xe = (max(0, x - d), x + d)
    for _ in range(n - 1):
        y, d = map(int, input().split())
        ye = (max(0, y - d), y + d)
        if ye[0] <= xe[0] and xe[1] <= ye[1]:
            xe = (xe[0], xe[1])
        elif xe[0] <= ye[0] and ye[1] <= xe[1]:
            xe = (ye[0], ye[1])
        else:
            if ye[1] >= xe[1]:
                if ye[0] <= xe[1]:
                    xe = (ye[0], xe[1])
                else:
                    print(-1)
                    exit(0)
            if xe[1] >= ye[1]:
                if xe[0] <= ye[1]:
                    xe = (xe[0], ye[1])
                else:
                    print(-1)
                    exit(0)
 
    print(xe[1])
