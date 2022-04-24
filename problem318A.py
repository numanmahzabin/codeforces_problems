# problem: https://codeforces.com/problemset/problem/318/A
import math
n, k = map(int, input().split())
if math.ceil(n / 2) >= k:
    print(k * 2 - 1)
else:
    k = k - int(math.ceil(n / 2))
    print(k * 2)
