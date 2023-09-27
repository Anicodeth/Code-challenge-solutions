def find_handle(val, handles, used):
    if val not in handles:
        return val
    return find_handle(handles[val], handles, used)

def main():
    n = int(input())
    handles = {}
    used = set()
    primary = []

    for _ in range(n):
        a, b = input().split()
        if a not in used:
            primary.append(a)

        if b not in used:
            handles[a] = b

        used.add(a)
        used.add(b)
    print(len(primary))
    for val in primary:
        pair = find_handle(val, handles, used)
        print(val, pair)


main()
