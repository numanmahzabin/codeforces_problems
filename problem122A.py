# problem: https://codeforces.com/problemset/problem/122/A
n = int(input())
for i in range(1, n + 1):
    s = str(i)
    is_lucky = 1
    for k in s:
        if k != '4' and k != '7':
            is_lucky = 0
            break
    if is_lucky:
        if n % i == 0:
            print('YES')
            break
if is_lucky == 0:
    print('NO')
