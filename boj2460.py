"""
0 32
3 13
28 25
17 5
21 20
11 0
12 12
4 2
0 8
21 0
"""

start = [0]
for i in range(10):
    busout, busin = map(int, input().split())
    now = start[-1] - busout + busin
    start.append(now)

print(sorted(start)[-1])

