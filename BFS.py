from collections import deque

g = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[], 'E':[], 'F':[]
}

q = deque(['A'])
v = set()

while q:
    n = q.popleft()
    if n in v: continue
    v.add(n)
    print(n)
    for x in g[n]:
        q.append(x)
