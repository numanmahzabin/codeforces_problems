# problem: https://codeforces.com/problemset/problem/1669/B
t = int(input())
for i in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split()))[:n], reverse=True)
    count = 1
    for k in range(n - 1):
        if a[k] == a[k + 1]:
            count += 1
        else:
            count = 1
        if count == 3:
            print(a[k - 1])
            break
    if count < 3:
        print('-1')
