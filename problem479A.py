# problem: https://codeforces.com/problemset/problem/479/A
a = int(input())
b = int(input())
c = int(input())

n = []
n.append(a + b + c)
n.append(a * b * c)
n.append((a + b) * c)
n.append(a * (b + c))
n.append((a * b) + c)
n.append(a + (b * c))
print(max(n))
