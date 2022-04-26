# problem: https://codeforces.com/problemset/problem/208/A
s = input()
s = s.replace('WUB', ' ').replace('  ', ' ').strip()
print(s)
'''
the below solution is also accepted

s = input()
song = ''
i = 0
spaces = 1
l = len(s)
while i < l:
    if s[i] == 'W' and i != l - 1:
        if s[i + 1] == 'U':
            if i != l - 2  and s[i + 2] == 'B':
                i += 3
                if spaces == 0:
                    song += ' '
                    spaces = 1
                continue
    
    song += s[i]
    spaces = 0
    i += 1
print(song.strip())
'''
