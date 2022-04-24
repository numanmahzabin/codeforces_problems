# problem: https://codeforces.com/problemset/problem/200/B
n = int(input())
p = list(map(int, input().split()))[:n]
x = 100 / n
percentage = 0
for i in p:
    if i != 0:
        percentage += x / (100 / i)
print('%.12f' % percentage)
