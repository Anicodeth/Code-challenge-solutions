for i in range(int(input())):
    a = int(input())
    if (a // 2) % 2 != 0:
        print('NO')
    else:
        e = list(range(2, a+1, 2))
        o = list(range(1, a+1, 2))
        if sum(e) == sum(o):
            print('YES')
            print(*e, end=' ')
            print(*o)
        else:
            o[-1] += sum(e) - sum(o)
            print('YES')
            print(*e, end=' ')
            print(*o)
