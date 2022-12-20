def swap_case(s):
    strr=""
    for c in s:
        if 65<=ord(c)<=90:
            strr+=chr(ord(c)+32)
        elif 97<=ord(c)<=122:
            strr+=chr(ord(c)-32)
        else:
            strr+=c
    return strr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
