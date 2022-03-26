# problem: https://codeforces.com/contest/231/problem/A
n = int(input())
count = 0
for x in range(0, n):
    a, b, c = list(map(int, input().split()))
    if a + b + c >= 2:
        count += 1
print(count)
