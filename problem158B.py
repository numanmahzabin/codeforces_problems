# problem: https://codeforces.com/problemset/problem/158/B
n = int(input())
members = list(map(int, input().split()))
count_1 = members.count(1)
count_2 = members.count(2)
count_3 = members.count(3)
count_4 = members.count(4)
taxi = count_4

while True:
    if count_3 - 1 >= 0 and count_1 - 1 >= 0:
        count_1 -= 1
        count_3 -= 1
        taxi += 1
    else:
        break
taxi += count_3

taxi += (count_2 * 2) // 4
count_2 -= ((count_2 * 2) // 4) * 2


if (count_2 * 2) + count_1 <= 4 and (count_2 * 2) + count_1 != 0:
    taxi += 1
else:
    taxi += ((count_2 * 2) + count_1) // 4
    if ((count_2 * 2) + count_1) % 4 != 0:
        taxi += 1


print(taxi)
