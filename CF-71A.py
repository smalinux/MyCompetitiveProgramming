# https://codeforces.com/contest/71/submission/118319255
x = int(input())
l = []
for i in range(x):
    s = input()
    l.append(s)

for r in l:
    if len(r) <= 10:
        print(f"{r}")
    else:
        print(f"{r[0]}{len(r)-2}{r[-1]}")
