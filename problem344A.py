# problem: https://codeforces.com/problemset/problem/344/A
n = int(input())
magnets = []
for i in range(n):
    magnets.append(int(input()))
count = 1
for i in range(n - 1):
    if magnets[i] != magnets[i + 1]:
        count += 1
print(count)
