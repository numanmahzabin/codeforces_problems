# problem: https://codeforces.com/problemset/problem/1669/C
t = int(input())


def is_possible(a):
    even_exist = odd_exist = 0
    for i in a:
        if i % 2 == 0:
            even_exist = 1
        if i % 2 != 0:
            odd_exist = 1
    if even_exist == 1 and odd_exist == 1:
        return 0
    else:
        return 1


for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    if is_possible(a):
        print('YES')
    else:
        for i in range(0, n, 2):
            a[i] += 1
        if is_possible(a):
            print('YES')
        else:
            print('NO')
