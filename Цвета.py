#контест по спортпроге за 22, там условия нельзя скачать(
import sys
 
 
try:
    sys.stdin = open('colors.in')
    sys.stdout = open('colors.out', 'w')
except:
    pass
 
n = int(input())
a = [int(x) for x in input().split()]
print(max(a) - min(a) + 1)
