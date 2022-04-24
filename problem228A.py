# problem: https://codeforces.com/problemset/problem/228/A
shoes = set(map(int, input().split()))
print(4 - len(shoes))

'''
# this code is also acceptable.
shoes = list(map(int, input().split()))
have_shoes = []
for i in shoes:
    if i not in have_shoes:
        have_shoes.append(i)
print(4 - len(have_shoes))
'''