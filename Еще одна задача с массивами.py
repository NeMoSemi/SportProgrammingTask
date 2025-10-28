import math
 
 
is_prime = [True] * (100100 + 1)
is_prime[0] = is_prime[1] = False
 
for i in range(2, int(100100 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 100100 + 1, i):
            is_prime[j] = False
 
primes = []
for i in range(2, 100100 + 1):
    if is_prime[i]:
        primes.append(i)
 
 
for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    gcd_all = 0
    for numb in a:
        gcd_all = math.gcd(gcd_all, numb)
 
    for numb in primes:
        if gcd_all % numb != 0:
            print(numb)
            break
