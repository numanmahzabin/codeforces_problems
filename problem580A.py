# problem: https://codeforces.com/problemset/problem/580/A
n = int(input())
m = 1
count = 1
seq = list(map(int, input().split()))
for i in range(n - 1):
    if seq[i] <= seq[i + 1]:
        count += 1
    else:
        m = max(m, count)
        count = 1
m = max(m, count)
print(m)
