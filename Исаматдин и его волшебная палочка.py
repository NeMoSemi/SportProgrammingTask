for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    is_one = False
    is_zero = False
    for x in a:
        if x % 2 == 0:
            is_zero = True
        else:
            is_one = True
        if is_one and is_zero:
            break
    if is_one and is_zero:
        print(*sorted(a))
    else:
        print(*a)
