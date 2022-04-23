# problem: https://codeforces.com/problemset/problem/705/A
n = int(input())
output = ''
for i in range(1, n + 1):
    output += 'I '
    if i % 2 == 0:
        output += 'love '
    else:
        output += 'hate '
    if i != n:
        output += 'that '
    else:
        output += 'it'
print(output)
